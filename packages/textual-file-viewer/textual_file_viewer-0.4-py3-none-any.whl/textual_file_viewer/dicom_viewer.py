from functools import lru_cache
from pathlib import Path
from typing import cast

import PIL.Image
import numpy as np
import pydicom
from pydicom.errors import InvalidDicomError
from pydicom.pixel_data_handlers import util
from rich.highlighter import RegexHighlighter
from rich_pixels import Pixels
from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.events import Resize
from textual.widgets import Static, Label, TabPane, TabbedContent
from textual_slider import Slider

from textual_file_viewer.dicom_tree import DicomTree

SUPPORTED_PHOTOMETRIC_INTERPRETATIONS = {'MONOCHROME1', 'MONOCHROME2', 'YBR_FULL_422'}


class DicomHighlighter(RegexHighlighter):
    """Highlights the text produced by pydicom. """

    base_style = "repr."
    highlights = [
        r"(?P<tag_start>\()(?P<attrib_name>.{4}),\s?(?P<attrib_value>.{4})(?P<tag_end>\)) (?P<str>.*) "
        r"(?P<none>([A-Z]{2})|([A-Z]{2}.[A-Z]{2})): (?P<number>.*)",
    ]


class DicomViewer(Static):
    def __init__(self) -> None:
        super().__init__()
        self.dataset: pydicom.dataset.Dataset | None = None
        self._selected_frame = -1
        self._total_frames = -1

    def compose(self) -> ComposeResult:
        with TabbedContent(id='dicom_viewer'):
            with TabPane('Image', id='tab_image'):
                with Vertical():
                    with Horizontal(id='slice_id_container', classes='remove'):
                        yield Label('X/Y', id='slice_id')
                        yield Slider(min=0, max=1, step=1, id='slice_id_slider')
                    yield Label(id='image_viewer')
            with TabPane('Tags', id='tab_tags'):
                yield DicomTree(id='dicom_tree')

    @on(Slider.Changed)
    def frame_changed(self, event: Slider.Changed) -> None:
        if self.dataset is None:
            return

        if event.value == self._selected_frame:
            return

        self._process_dicom_image()

    def on_resize(self, _: Resize) -> None:
        if self.dataset is None:
            return

        self.call_after_refresh(self._process_dicom_image)

    def load_dicom(self, filename: Path) -> None:
        try:
            self.dataset = cast(pydicom.Dataset, pydicom.dcmread(filename))
        except InvalidDicomError:
            self.dataset = None
            return

        self.query_one('#dicom_tree', DicomTree).set_dataset(self.dataset)

        frames = pydicom.pixels.utils.get_nr_frames(self.dataset)

        container = self.query_one('#slice_id_container', Horizontal)
        slider = self.query_one('#slice_id_slider', Slider)
        if frames <= 1:
            container.set_class(True, 'remove')
            self._selected_frame = 0
            self._total_frames = 0
        else:
            container.set_class(False, 'remove')
            self._total_frames = frames - 1
            slider.max = self._total_frames
            self._selected_frame = frames // 2

        slider.value = self._selected_frame
        self._process_dicom_image()

        self.query_one('#dicom_viewer', TabbedContent).active = 'tab_image'

    def _process_dicom_image(self) -> None:
        if self.dataset is None:
            return

        if self.dataset.PhotometricInterpretation not in SUPPORTED_PHOTOMETRIC_INTERPRETATIONS:
            self.notify(message=f'Only {" ".join(SUPPORTED_PHOTOMETRIC_INTERPRETATIONS)} are supported',
                        title='No image view',
                        severity='warning')
            return

        if self._total_frames > 0:
            self._selected_frame = self.query_one('#slice_id_slider', Slider).value
        im = self._get_frame(self._selected_frame)

        self.query_one('#slice_id', Label).update(f'{self._selected_frame}/{self._total_frames}')

        image_viewer = self.query_one('#image_viewer', Label)
        width = image_viewer.container_viewport.width
        height = image_viewer.container_viewport.height * 2  # Don't know why times 2, but it seems to work

        try:
            im.thumbnail((width, height))
        except ZeroDivisionError:
            return

        self.query_one('#image_viewer', Label).update(Pixels.from_image(im))

    @lru_cache(maxsize=512)
    def _get_frame(self, frame_id: int) -> PIL.Image.Image:
        assert self.dataset is not None

        match len(self.dataset.pixel_array.shape), self.dataset.PhotometricInterpretation:
            case (4, 'YBR_FULL_422') | (3, _):
                np_array = self.dataset.pixel_array[frame_id]
            case _:
                np_array = self.dataset.pixel_array

        match self.dataset.PhotometricInterpretation:
            case 'MONOCHROME1':
                # minimum is white, maximum is black
                # (https://dicom.innolitics.com/ciods/ct-image/image-pixel/00280004)
                np_array = pydicom.pixel_data_handlers.apply_voi_lut(np_array, self.dataset)
                minimum, maximum = np.amin(np_array), np.amax(np_array)
                np_array = (maximum - np_array) * 255.0 / (maximum - minimum)
            case 'MONOCHROME2':
                center, width = self.dataset.WindowCenter, self.dataset.WindowWidth
                minimum, maximum = center - width / 2, center + width / 2
                np_array[np_array < minimum] = minimum
                np_array[np_array > maximum] = maximum
                np_array = (np_array - minimum) * 255.0 / (maximum - minimum)
            case 'YBR_FULL_422':
                np_array = util.convert_color_space(np_array, 'YBR_FULL', 'RGB')
            case _:
                pass

        return PIL.Image.fromarray(np_array).convert('RGB')  # type: ignore
