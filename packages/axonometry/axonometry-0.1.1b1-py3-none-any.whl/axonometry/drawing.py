# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Where all operations are recorded."""

from typing import Never

from compas.geometry import Line as CLine
from compas.geometry import Point as CPoint
from compas.geometry import Polyline as CPolyline
from vpype import Document, LineCollection, circle, write_svg
from vpype_cli import execute

from .config import config


class Drawing:
    """I record all what is happening.

    I am basically a wrapper of a vpype.Document adding custom methods.
    """

    def __init__(self, page_format: str = "A1", page_layout: str = "portrait") -> None:  # noqa: D107
        self.dimensions = config.din[page_format][page_layout]
        self.document = Document(page_size=self.dimensions)  #: Wrapper for a vpype.Document
        self.traces = []

    def resizet_page(self, page_format: str, page_layout: str) -> Never:
        """Not implemented."""
        raise NotImplementedError

    def add(self, item, layer_id: int | None = None) -> None:
        """Adding geometries to the drawing."""
        self.traces.append(item)
        compas_data = [item.data]  # it's the compas data which is being drawn
        self.add_compas_geometry(compas_data)
        # config.logger.debug(f"[{item.key.upper()}] {item} added to {self}.")
        # geometry = self.__convert_compas_to_vpype_lines(compas_data)
        # self.document.add(geometry)

    def show(self) -> None:
        """Show the drawing with the vpype viewer."""
        # move geometry into center of page
        self.document.translate(self.dimensions[0] / 2, self.dimensions[1] / 2)
        execute("show --colorful", document=self.document)

    def save_svg(self, filepath: str) -> None:
        """Save the drawing to an SVG file."""
        # use vpype to save file
        write_svg(output=filepath, document=self.document, center=True)

    def add_axonometry(self, axo, position: tuple | None = None) -> None:
        """Combine several axonometries in a single drawing."""
        if position:
            axo.drawing.document.translate()  # TODO compute translate from new position
        self.document.extend(axo.drawing.document)

    def add_compas_geometry(self, compas_data) -> None:
        """Add directly compas geometries to the drawing."""
        # no traces ?
        config.logger.debug(f"[{self}] Add compas data objects to drawing: {compas_data}")
        geometry = self.__convert_compas_to_vpype_lines(compas_data)
        self.document.add(geometry)

    def __convert_compas_to_shapely(self, compas_geometry):
        """Convert a compas geometry object to a shapely LineString."""
        from shapely import LineString

        if isinstance(compas_geometry, CLine):
            return LineString(
                [
                    (
                        compas_geometry.start.x * config.css_pixel,
                        compas_geometry.start.y * config.css_pixel,
                    ),
                    (
                        compas_geometry.end.x * config.css_pixel,
                        compas_geometry.end.y * config.css_pixel,
                    ),
                ],
            )
        if isinstance(compas_geometry, CPolyline):
            return LineString(
                [
                    (point.x * config.css_pixel, point.y * config.css_pixel)
                    for point in compas_geometry
                ],
            )
        if isinstance(compas_geometry, CPoint):
            # TODO: radius exagerated for now. later smaller or pass ?
            return circle(
                compas_geometry.x * config.css_pixel,
                compas_geometry.y * config.css_pixel,
                10,
            )
        raise ValueError("Unsupported Compas geometry type")

    def __convert_compas_to_vpype_lines(self, compas_geometries) -> LineCollection:
        """Convert a list of compas geometries to a vpype LineCollection."""
        vpype_lines = LineCollection()
        for compas_geometry in compas_geometries:
            shapely_line = self.__convert_compas_to_shapely(compas_geometry)
            vpype_lines.append(shapely_line)
        return vpype_lines

    def __repr__(self) -> str:
        """Identify drawing."""
        return "Drawing"  # + hex(id(self)) ?
