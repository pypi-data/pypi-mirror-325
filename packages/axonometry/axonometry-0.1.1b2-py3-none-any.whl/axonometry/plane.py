# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
from typing import TYPE_CHECKING

from compas.geometry import Line as CLine
from compas.geometry import Point as CPoint
from compas.geometry import Vector as CVector
from compas.geometry import intersection_line_line_xy

from .config import config
from .line import Line
from .point import Point

if TYPE_CHECKING:
    from .trihedron import Trihedron


class Plane:
    """Base class for axonometric and reference planes."""

    def __init__(self) -> None:  # noqa: D107
        self.key = None
        self.drawing = None  # Initialize the drawing attribute if needed
        self.objects = []

    def add_point(self, point: Point) -> Point:
        """Add a point to the current plane."""
        assert point.key == self.key, (
            f"Point coordinates must follow containing plane coordinates. Plane:{self.key} & Point:{point.key}"
        )
        if self.key == "xyz":
            # Point data could not exist
            config.logger.debug(
                f"[{self.key.upper()}] Adding {point} by auxilary projection.",
            )
            if point.data is None:
                point.data = self.__decompose_axo_point(point)

        else:
            point.data = point.data.transformed(self.matrix)

        config.logger.info(f"[{self.key.upper()}] Add {point}")
        self.objects.append(point)
        self.drawing.add(point)
        point.plane = self  # add self as parent
        config.logger.debug(f"[{self.key.upper()}] Current objects in {self}: {self.objects}.")
        return point

    def add_line(self, line: Line) -> Line:
        """Add a line to the current reference plane."""
        assert line.key == self.key, (
            f"Line coordinates must coorespond to plane coordinates system. Plane:{self.key=} & Point:{line.key=}"
        )

        line.start = self.add_point(line.start)
        line.end = self.add_point(line.end)
        line.data = CLine(line.start.data, line.end.data)
        self.objects.append(line)
        self.drawing.add(line)
        line.plane = self

        if self.key == "xyz":
            # One level of recursivity
            for ref_plane_key in self.__common_projections(
                line.start.projections,
                line.end.projections,
            ):
                print(ref_plane_key)
                auxilary_line = Line(
                    line.start.projections[ref_plane_key]._reset_data(),
                    line.end.projections[ref_plane_key]._reset_data(),
                )
                self.reference_planes[ref_plane_key].add_line(auxilary_line)

        # TODO: update line.projections

        return line

    def __common_projections(self, dict1, dict2):
        """Find which projected points are on the same reference plane."""
        for key in dict1:
            if key == "xyz":  # Exclude this specific key from comparison
                continue
            if key in dict2 and dict1[key] is not None and dict2[key] is not None:
                yield key

    def __decompose_axo_point(self, axo_point: Point) -> CPoint:
        """When a point is added in XYZ space it becomes the intersection of two points.

        Basically adding points in two (random) reference planes and intersecting them
        in the xyz space. That intersection becomes the drawn points' data.
        """
        config.logger.debug(f"Decompose {axo_point=}")

        # make two points
        keys = ["xy", "yz", "zx"]
        k1, k2 = random.sample(keys, 2)

        if k1 == "zx" or k2 == "zx":
            config.logger.debug(f"Case 1 {k1=} {k2=}")
            p1 = Point(x=axo_point.x, y=axo_point.y)
            p2 = Point(y=axo_point.y, z=axo_point.z)
            plane1 = self.reference_planes["xy"]
            plane2 = self.reference_planes["yz"]

        if k1 == "yz" or k2 == "yz":
            config.logger.debug(f"Case 2 {k1=} {k2=}")
            p1 = Point(x=axo_point.x, y=axo_point.y)
            p2 = Point(z=axo_point.z, x=axo_point.x)
            plane1 = self.reference_planes["xy"]
            plane2 = self.reference_planes["zx"]

        if k1 == "xy" or k2 == "xy":
            config.logger.debug(f"Case 3 {k1=} {k2=}")
            p1 = Point(z=axo_point.z, x=axo_point.x)
            p2 = Point(y=axo_point.y, z=axo_point.z)
            plane1 = self.reference_planes["zx"]
            plane2 = self.reference_planes["yz"]

        config.logger.debug(f"Two auxilary points computed {p1=}, {p2=}")

        plane1.add_point(p1)  # ISSUE IS HERE
        plane2.add_point(p2)
        axo_point.projections[p1.plane.key] = p1
        axo_point.projections[p2.plane.key] = p2

        # add them in respective ReferencePlanes
        axo_point_data = intersection_line_line_xy(
            CLine.from_point_and_vector(p1.data, plane1.projection_vector),
            CLine.from_point_and_vector(p2.data, plane2.projection_vector),
        )
        axo_point_data = CPoint(*axo_point_data)
        config.logger.debug(f"New {axo_point_data=}")
        # Add points in reference planes to the
        # axo point projections collection

        # draw intersection
        self.drawing.add_compas_geometry(
            [CLine(p1.data, axo_point_data), CLine(p2.data, axo_point_data)],
        )
        return axo_point_data


class ReferencePlane(Plane):
    """Represents a reference plane in an axonometric projection.

    :param lines: The two lines making up the reference plane axes.

    """

    def __init__(self, line_pair: list[CLine], projection_vector: CVector) -> None:  # noqa: D107
        super().__init__()  # Call the parent class constructor if necessary
        self.trihedron: Trihedron | None = None
        self.matrix = None
        self.axes = line_pair
        self.projection_vector = projection_vector
        self.matrix_to_coord_plane = None  # TODO

    def __repr__(self) -> str:
        """Get axes keys."""
        return f"Reference Plane {self.key.upper()}"

    def add_svg_file(self, svg_file: str):
        """Get an external svg and add it to current reference plane.

        An SVG is treated as a collection of lines. The steps to follow are extracting the line
        coordinates and adding each line to the current plane. Roughly the code should be as
        follow::

            for line in collection:
                self.add_line(Line(line))  # this will call the matrix
            doc = self.drawing.convert_svg_vpype_doc(svg_file)
        """
        raise NotImplementedError
