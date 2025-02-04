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

if TYPE_CHECKING:
    from .trihedron import Trihedron


class Projectile:
    """I'm a geometry which is beeing projected around an Axonometry.

    TODO: Implement names and selection by name.

    """

    def __init__(self) -> None:  # noqa: D107
        self.plane = None  # plane membership is set by parent object
        self.projections = {"xy": None, "yz": None, "zx": None, "xyz": []}


class Point(Projectile):
    """Wrapper for a :ref:`~compas.geometry.Point`.

    The coordinates have to be passed on explicitly::

        Point(x=10, y=20)
        Point(z=15, y=20)
        Point(x=10, z=15)
        Point(x=10, y=20, z=15)

    :param kwargs: A minimum of two coordanate values.
    :raises ValueError: A point is described by a minimum of two coordinates.

    """

    def __init__(self, **kwargs: float) -> None:  # noqa: D107
        super().__init__()
        if len(kwargs) == 1:
            # If only one coordinate is provided, raise an error.
            raise ValueError("At least two coordinates must be provided.")
        self.plane = None  # set by parent
        self.x: float | None = kwargs.get("x")  #: User defined axonometric coordainate.
        self.y: float | None = kwargs.get("y")  #: User defined axonometric coordainate.
        self.z: float | None = kwargs.get("z")  #: User defined axonometric coordainate.
        combined_key = ""
        if self.x is not None:
            combined_key += "x"
        if self.y is not None:
            combined_key += "y"
        if self.z is not None:
            combined_key += "z"
        self.key: str = combined_key  #: The plane membership key.
        self.key = "zx" if self.key == "xz" else self.key  # switch order for xz
        # the point which is drawn on the paper
        self.data: CPoint | None = None  #: Axonooetry plane case
        if self.key == "xy":
            self.data = CPoint(self.x, self.y)
        elif self.key == "yz":
            self.data = CPoint(self.z, self.y)
        elif self.key == "zx":
            self.data = CPoint(self.x, self.z)
        # else:
        #     self.data: CPoint = None  # CPoint(self.x, self.y, self.z)
        # """Internal data of the point, see :ref:`implementation` for details."""

    def project(
        self,
        distance: float | None = None,
        ref_plane_key: str | None = None,
    ) -> "Point":
        """Project current point on another plane.

        :param distance: The missing third coordinate in order to project the point on the
            axonometric picture plane. This applies when the point to project is contained
            in a reference plane.
        :param ref_plane_key: The selected reference plane on which to project the point. This
            applies when the point to project is on the axonometric picture plane.
        """
        # determine projection origin plane
        if self.plane.key == "xyz":
            assert ref_plane_key, (
                "Provide reference plane key in order to project a point from the XYZ space."
            )
            new_point = None
            config.logger.debug(
                f"{self=} has already these projections {self.projections=}",
            )
            if ref_plane_key == "xy":
                # Point was maybe already projected when added to the XYZ axo space
                if self.projections["xy"]:
                    existing_projected_point = self.projections[
                        "xy"
                    ]  # TODO: use __contains__ ?
                else:
                    new_point = self.plane.reference_planes[ref_plane_key].add_point(
                        Point(x=self.x, y=self.y),
                    )
            elif ref_plane_key == "yz":
                # Point was maybe already projected when added to the XYZ axo space
                if self.projections["yz"]:
                    existing_projected_point = self.projections[
                        "yz"
                    ]  # TODO: use __contains__ ?
                else:
                    new_point = self.plane.reference_planes[ref_plane_key].add_point(
                        Point(y=self.y, z=self.z),
                    )
            elif ref_plane_key == "zx":
                # Point was maybe already projected when added to the XYZ axo space
                if self.projections["zx"]:
                    existing_projected_point = self.projections[
                        "zx"
                    ]  # TODO: use __contains__ ?
                else:
                    new_point = self.plane.reference_planes[ref_plane_key].add_point(
                        Point(x=self.x, z=self.z),
                    )

            # Add line to drawing is projection is new
            if new_point:
                self.plane.drawing.add_compas_geometry(
                    [CLine(self.data, new_point.data)],
                )
                self.projections[ref_plane_key] = new_point
            else:
                new_point = existing_projected_point  # for the return

        else:
            # projection initiated from a reference plane
            assert distance is not None, (
                "Provide (third coordinate value) in order to project the point into XYZ space."
            )
            if self.plane.key == "xy":
                new_point = Point(x=self.x, y=self.y, z=distance)  # data will be update
                ref_plane_key = random.choice(["yz", "zx"])  # noqa: S311
                if ref_plane_key == "yz":
                    auxilary_point = self.plane.axo.reference_planes[ref_plane_key].add_point(
                        Point(y=self.y, z=distance),
                    )
                elif ref_plane_key == "zx":
                    auxilary_point = self.plane.axo.reference_planes[ref_plane_key].add_point(
                        Point(x=self.x, z=distance),
                    )
            elif self.plane.key == "yz":
                new_point = Point(x=distance, y=self.y, z=self.z)  # data will be update
                ref_plane_key = random.choice(["zx", "xy"])  # noqa: S311
                if ref_plane_key == "zx":
                    auxilary_point = self.plane.axo.reference_planes[ref_plane_key].add_point(
                        Point(z=self.z, x=distance),
                    )
                elif ref_plane_key == "xy":
                    auxilary_point = self.plane.axo.reference_planes[ref_plane_key].add_point(
                        Point(y=self.y, x=distance),
                    )
            elif self.plane.key == "zx":
                new_point = Point(x=self.x, y=distance, z=self.z)  # data will be update
                ref_plane_key = random.choice(["xy", "yz"])  # noqa: S311
                if ref_plane_key == "xy":
                    auxilary_point = self.plane.axo.reference_planes[ref_plane_key].add_point(
                        Point(x=self.x, y=distance),
                    )
                elif ref_plane_key == "yz":
                    auxilary_point = self.plane.axo.reference_planes[ref_plane_key].add_point(
                        Point(z=self.z, y=distance),
                    )

            axo_point_data = intersection_line_line_xy(
                CLine.from_point_and_vector(self.data, self.plane.projection_vector),
                CLine.from_point_and_vector(
                    auxilary_point.data,
                    self.plane.axo.reference_planes[ref_plane_key].projection_vector,
                ),
            )

            new_point.data = CPoint(*axo_point_data)
            # draw intersection
            self.plane.drawing.add_compas_geometry(
                [
                    CLine(self.data, axo_point_data),
                    CLine(auxilary_point.data, axo_point_data),
                ],
            )

            self.plane.axo.add_point(new_point)
            self.projections[ref_plane_key] = new_point
        # TODO: update point projection collection
        return new_point

    @property
    def __data__(self) -> list:
        """Give access to data in order to be used with compas methods."""
        return list(self.data)

    def __repr__(self) -> str:
        """Get the user set coordinate values."""
        if self.key == "xy":
            repr_str = f"Point(x={self.x}, y={self.y})"
        elif self.key == "yz":
            repr_str = f"Point(y={self.y}, z={self.z})"
        elif self.key == "zx":
            repr_str = f"Point(x={self.x}, z={self.z})"
        else:
            repr_str = f"Point(x={self.x}, y={self.y}, z={self.z})"

        return repr_str

    def __eq__(self, other: "Point") -> bool:
        """Projected points are considered as equal."""
        if not isinstance(other, type(self)):
            # if the other item of comparison is not also of the Point class
            return TypeError(f"Can't compare {self} and {other}")
        if self.key == other.key:
            return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        common_key = "".join(set(self.key).intersection(other.key))
        if set(common_key) == set("xy"):
            return (self.x == other.x) and (self.y == other.y)
        if set(common_key) == set("yz"):
            return (self.y == other.y) and (self.z == other.z)
        if set(common_key) == set("zx"):
            return (self.x == other.x) and (self.z == other.z)
        return False


class Line:
    """To be implemented soon."""

    def __init__(self):  # noqa: D107
        pass


class Surface:
    """To be implemented soon."""

    def __init__(self):  # noqa: D107
        pass


class Plane:
    """Base class for axonometric and reference planes."""

    def __init__(self) -> None:  # noqa: D107
        self.key = None
        self.matrix = None
        self.drawing = None  # Initialize the drawing attribute if needed
        self.objects = []

    def add_point(self, point: Point) -> Point:
        """Add a point to the current plane."""
        assert point.key == self.key, (
            f"Point coordinates must follow containing plane coordinates. Plane:{self.key} & Point:{point.key}"
        )
        if set(self.key) == set("xyz"):
            # Point data could not exist
            config.logger.debug(
                f"[{self.key.upper()}] Adding {point} to XYZ space. If {point.data=} has not been computed before, add auxilary projection.",
            )
            if point.data is None:
                point.data = self._decompose_axo_point(point)

        else:
            point.data = point.data.transformed(self.matrix)

        config.logger.info(f"[{self.key.upper()}] Add {point}")
        self.objects.append(point)
        self.drawing.add(point)
        point.plane = self  # add self as parent
        config.logger.debug(f"[{self.key.upper()}] Current objects in {self}: {self.objects}.")
        return point

    def _decompose_axo_point(self, axo_point: Point) -> CPoint:
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
        self.axes = line_pair
        self.projection_vector = projection_vector
        self.matrix_to_coord_plane = None  # TODO

    def __repr__(self) -> str:
        """Get axes keys."""
        return f"Reference Plane {self.key.upper()}"
