"""Where all operations are recorded."""
# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import TYPE_CHECKING

from compas.geometry import Geometry as CGeometry
from compas.scene import Scene as CScene
from vpype import Document

from .config import config
from .utils import _convert_compas_to_vpype_lines

if TYPE_CHECKING:
    from .axonometry import Axonometry


class Drawing:
    """I record all what is happening.

    Basically a wrapper for vpype.Document and compas.scene.Scene objects.
    The various add_* functions at the Axonometry/Reference Plane level
    interact mostly with this object.
    """

    def __init__(self, page_format: str = "A1", page_layout: str = "portrait") -> None:  # noqa: D107
        self.dimensions = config.din[page_format][page_layout]
        self.document = Document(page_size=self.dimensions)  #: Wrapper for a vpype.Document
        self.scene = CScene()

    def resize_page(self, page_format: str, page_layout: str) -> None:
        """Not implemented."""
        raise NotImplementedError

    def add(self, item, layer_id: int | None = None) -> None:
        """Adding geometries to the drawing."""
        compas_data = [item.data]  # it's the compas data which is being drawn
        config.logger.debug(f"[{item.key.upper()}] {item} added to {self}.")
        self.add_compas_geometry(compas_data)

    def add_axonometry(self, axo: "Axonometry", position: tuple | None = None) -> None:
        """Combine several axonometries in a single drawing."""
        if position:
            axo.drawing.document.translate()  # TODO compute translate from new position
        self.document.extend(axo.drawing.document)

    def add_compas_geometry(self, compas_data: list[CGeometry]) -> None:
        """Add directly compas geometries to the drawing."""
        # no traces ?
        config.logger.debug(f"[{self}] Add compas data objects to drawing: {compas_data}")
        for item in compas_data:
            self.scene.add(item)
        geometry = _convert_compas_to_vpype_lines(compas_data)
        self.document.add(geometry)

    def __repr__(self) -> str:
        """Identify drawing."""
        return "Drawing"  # + hex(id(self)) ?
