import dataclasses
from pathlib import Path
from typing import cast

import PIL.Image
import SimpleITK as sitk
import numpy as np
from rich.markdown import Markdown
from rich_pixels import Pixels
from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, ScrollableContainer
from textual.events import Resize
from textual.widgets import Static, Label, TabPane, TabbedContent
from textual_slider import Slider


@dataclasses.dataclass
class SlicePhaseId:
    slice_id: int | None = None
    phase_id: int | None = None


class MhdNiftiViewer(Static):
    def __init__(self) -> None:
        super().__init__()
        self.dataset: sitk.Image | None = None
        self._array: np.ndarray | None = None
        self.index = SlicePhaseId()
        self._image_range = (-1, -1)

    def compose(self) -> ComposeResult:
        with TabbedContent(id='image_viewer'):
            with TabPane('Image', id='tab_image'):
                with Vertical():
                    with Horizontal(id='phase_id_container', classes='remove'):
                        yield Label('PH:    ', id='phase_id')
                        yield Slider(min=0, max=1, step=1, id='phase_id_slider')
                    with Horizontal(id='slice_id_container', classes='remove'):
                        yield Label('SL:    ', id='slice_id')
                        yield Slider(min=0, max=1, step=1, id='slice_id_slider')
                    yield Label(id='image_viewer')
            with TabPane('Tags', id='tab_tags'):
                yield ScrollableContainer(Label(id='image_tags'))

    @on(Slider.Changed)
    def frame_changed(self, _: Slider.Changed) -> None:
        if self.dataset is None:
            return

        slice_id_slider = self.query_one('#slice_id_slider', Slider)
        phase_id_slider = self.query_one('#phase_id_slider', Slider)
        new_index = SlicePhaseId(
            slice_id_slider.value if not slice_id_slider.has_class('remove') else None,
            phase_id_slider.value if not phase_id_slider.has_class('remove') else None
        )

        if new_index == self.index:
            return

        self.query_one('#slice_id', Label).update(f'Sl: {new_index.slice_id:3}/{slice_id_slider.max:3}')
        self.query_one('#phase_id', Label).update(f'Ph: {new_index.phase_id:3}/{phase_id_slider.max:3}')

        self.index = new_index

        self._process_image()

    def on_resize(self, _: Resize) -> None:
        if self.dataset is None:
            return

        self.call_after_refresh(self._process_image)

    def load_image(self, filename: Path) -> None:
        self.dataset = sitk.ReadImage(filename)
        array = sitk.GetArrayFromImage(self.dataset)
        self._image_range = (np.amin(array), np.amax(array))
        self._array = (array - self._image_range[0]) * 255.0 / (self._image_range[1] - self._image_range[0])

        slice_id_container = self.query_one('#slice_id_container', Horizontal)
        slice_id_slider = self.query_one('#slice_id_slider', Slider)
        phase_id_container = self.query_one('#phase_id_container', Horizontal)
        phase_id_slider = self.query_one('#phase_id_slider', Slider)

        match cast(int, self.dataset.GetDimension()):  # type: ignore
            case 2:
                slice_id_container.set_class(True, 'remove')
                phase_id_container.set_class(True, 'remove')
            case 3:
                slice_id_slider.max = cast(int, self.dataset.GetSize()[2]) - 1  # type: ignore
                slice_id_container.set_class(slice_id_slider.max <= 1, 'remove')
                phase_id_container.set_class(True, 'remove')
            case 4:
                slice_id_slider.max = cast(int, self.dataset.GetSize()[2]) - 1  # type: ignore
                phase_id_slider.max = cast(int, self.dataset.GetSize()[3]) - 1  # type: ignore
                slice_id_container.set_class(slice_id_slider.max <= 1, 'remove')
                phase_id_container.set_class(phase_id_slider.max <= 1, 'remove')

        markdown = ['|Key|Value|', '|--|--|']
        for k in self.dataset.GetMetaDataKeys():  # type: ignore
            markdown.append(f'|{k}|{self.dataset.GetMetaData(k)}|')  # type: ignore

        self.query_one('#image_tags', Label).update(Markdown('\n'.join(markdown)))
        self.query_one('#image_viewer', TabbedContent).active = 'tab_image'

    def _process_image(self) -> None:
        slice_id_slider = self.query_one('#slice_id_slider', Slider)
        phase_id_slider = self.query_one('#phase_id_slider', Slider)

        assert self._array is not None
        match cast(int, self.dataset.GetDimension()):  # type: ignore
            case 2:
                im = PIL.Image.fromarray(self._array).convert('RGB')
            case 3:
                im = PIL.Image.fromarray(self._array[slice_id_slider.value]).convert('RGB')
            case 4:
                im = PIL.Image.fromarray(self._array[phase_id_slider.value][slice_id_slider.value]).convert('RGB')
            case _:
                raise RuntimeError('Unsupported dimension (<2, >4).')

        image_viewer = self.query_one('#image_viewer', Label)
        width = image_viewer.container_viewport.width
        height = image_viewer.container_viewport.height * 2  # Don't know why times 2, but it seems to work

        try:
            im.thumbnail((width, height))
            self.query_one('#image_viewer', Label).update(Pixels.from_image(im))
        except ZeroDivisionError:
            pass
