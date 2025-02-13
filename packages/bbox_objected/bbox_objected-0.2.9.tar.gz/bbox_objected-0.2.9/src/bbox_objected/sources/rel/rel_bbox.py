from __future__ import annotations

from typing import TYPE_CHECKING

from ..bbox_img import BBoxImgMixin
from .editor import RelBBoxEditor

if TYPE_CHECKING:
    from collections.abc import Sequence

    import numpy as np
    import numpy.typing as npt
    from cv2.typing import MatLike

    from ...annotations import BBoxKind


class RelBBox(RelBBoxEditor, BBoxImgMixin):
    _REL_VALIDATION_ERROR = "Invalid coords passed. Use only float coords in range [0, 1]"

    def __init__(
        self,
        coords: Sequence,
        kind: BBoxKind | str = "x1y1x2y2",
        text: str = "",
    ) -> None:
        super().__init__(coords, kind)
        self.text = text

    def crop_from(self, img: npt.NDArray) -> npt.NDArray:
        h, w, *_ = img.shape
        x1 = round(self.x1 * w)
        x2 = round(self.x2 * w)
        y1 = round(self.y1 * h)
        y2 = round(self.y2 * h)

        return img[y1:y2, x1:x2]

    def is_valid(self) -> bool:
        if not (
            (0.0 <= self.x1 <= 1.0)
            and (0.0 <= self.y1 <= 1.0)
            and (0.0 <= self.x2 <= 1.0)
            and (0.0 <= self.y2 <= 1.0)
        ):
            raise ValueError(self._REL_VALIDATION_ERROR)

        return super().is_valid()

    def as_abs(self, img_w: int, img_h: int):  # noqa: ANN201
        from ..abs.abs_bbox import AbsBBox  # noqa: PLC0415

        x1, y1, x2, y2 = self.get_x1y1x2y2()
        x1 = round(x1 * img_w)
        y1 = round(y1 * img_h)
        x2 = round(x2 * img_w)
        y2 = round(y2 * img_h)
        return AbsBBox((x1, y1, x2, y2), text=self.text)

    def show_on(self, img: npt.NDArray[np.uint8] | MatLike) -> None:
        h, w, *_ = img.shape
        self.__show_on(self.as_abs(img_w=w, img_h=h).get_x1y1x2y2(), img, self.text)

    def __repr__(self) -> str:
        bbox = (
            f"RelBBox(x1={round(self.x1, 3)}, y1={round(self.y1, 3)}, "
            f"x2={round(self.x2, 3)}, y2={round(self.y2, 3)})"
        )
        if text := self.text:
            text = f" - {self.text}"
        return f"<{bbox}{text}>"
