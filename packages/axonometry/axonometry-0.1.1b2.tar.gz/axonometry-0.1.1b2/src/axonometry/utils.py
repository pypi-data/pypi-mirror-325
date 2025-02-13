"""I/O, visualizing and converting functions."""
# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import TYPE_CHECKING

from compas.geometry import Geometry as CGeometry
from compas.geometry import Line as CLine
from compas.geometry import Point as CPoint
from compas.geometry import Polyline as CPolyline
from shapely import LineString
from vpype import Document, LineCollection, circle, read_svg, write_svg
from vpype_cli import execute

if TYPE_CHECKING:
    from .axonometry import Axonometry

from .config import config


def _convert_compas_to_shapely(compas_geometry: CGeometry) -> LineString:
    """Convert a compas geometry object to a shapely LineString."""
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


def _convert_svg_vpype_doc(svg_file: str) -> Document:
    """Create a vpype Document from a list of Compas geometries."""
    coll = read_svg(svg_file, 0.01)[0].as_mls()
    points = []
    for line in coll.geoms:
        for coord in line.coords:
            points.append(coord)

    compas_geometries = [CPolyline(points)]
    layers = _convert_compas_to_vpype_lines(compas_geometries)
    document = Document()
    for layer in layers:
        document.add(layer, layer_id=1)  # Assuming all lines are on the same layer
    return document


def _convert_compas_to_vpype_lines(
    compas_geometries: list[CGeometry],
) -> LineCollection:
    """Convert a list of compas geometries to a vpype LineCollection."""
    vpype_lines = LineCollection()
    for compas_geometry in compas_geometries:
        shapely_line = _convert_compas_to_shapely(compas_geometry)
        vpype_lines.append(shapely_line)
    return vpype_lines


def save_svg(axonometry: "Axonometry", filepath: str) -> None:
    """Save the drawing to an SVG file."""
    doc = axonometry.drawing.document
    # use vpype to save file
    write_svg(output=filepath, document=doc, center=True)


def save_json(axonometry: "Axonometry", filepath: str) -> None:
    """Dump the scene data to a json file."""
    scene = axonometry.drawing.scene
    scene.to_json(filepath, pretty=False)


def visualize(axonometry: "Axonometry") -> None:
    """Have a look at the geometry with the compas viewer or other context."""
    raise NotImplementedError


def show_paths(axonometry: "Axonometry") -> None:
    """Show the drawing paths with the vpype viewer."""
    # move geometry into center of page
    # TODO: this breaks the use of drawing.extend !
    # prevents from calling the function while script is executed.
    axonometry.drawing.document.translate(
        axonometry.drawing.dimensions[0] / 2,
        axonometry.drawing.dimensions[1] / 2,
    )
    execute("show --colorful", document=axonometry.drawing.document)
