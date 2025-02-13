# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

from compas.geometry import Line as CLine
from compas.geometry import Point as CPoint
from compas.geometry import intersection_line_line_xy

from .config import config


class Point:
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
        if len(kwargs) == 1:
            # If only one coordinate is provided, raise an error.
            raise ValueError("At least two coordinates must be provided.")
        self.plane = None  # set by parent
        self.projections = {"xy": None, "yz": None, "zx": None, "xyz": []}
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

    def _reset_data(self):
        self.data: CPoint | None = None  #: Axonooetry plane case
        if self.key == "xy":
            self.data = CPoint(self.x, self.y)
        elif self.key == "yz":
            self.data = CPoint(self.z, self.y)
        elif self.key == "zx":
            self.data = CPoint(self.x, self.z)
        return self

    def project(
        self,
        distance: float | None = None,
        ref_plane_key: str | None = None,
    ) -> "Point":
        """Project current point on another plane.

        Two scenarios: current point is in a reference plane and is projected onto the
        axonometric picture plane. Or the current point is in the axonometric picture
        plane and is beeing projected on a reference plane. Depending, the right paramteres
        have to be provided.

        :param distance: The missing third coordinate in order to project the point on the
            axonometric picture plane. This applies when the point to project is contained
            in a reference plane.
        :param ref_plane_key: The selected reference plane on which to project the point. This
            applies when the point to project is on the axonometric picture plane.
        """
        # determine projection origin plane
        if self.plane.key == "xyz":
            config.logger.debug(f"{self} is in XYZ and projected on a reference plane")
            new_point = self._project_on_reference_plane(ref_plane_key)
        else:
            config.logger.debug(
                f"{self} is in {self.plane} and projected on a reference plane",
            )
            new_point = self._project_on_axonometry_plane(distance)

        return new_point

    def _project_on_axonometry_plane(self, distance: float) -> "Point":
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

        # Update point projections collection
        new_point.projections[ref_plane_key] = auxilary_point
        new_point.projections[self.plane.key] = self
        auxilary_point.projections["xyz"].append(new_point)
        self.projections["xyz"].append(new_point)

        return new_point

    def _project_on_reference_plane(self, ref_plane_key: str) -> "Point":
        if self == self.projections[ref_plane_key]:
            # projection of point already exists, nothing to do
            config.logger.debug(
                f"{self=} is already projected in {ref_plane_key.upper()}: {self.projections[ref_plane_key]=}",
            )
            new_point = self.projections[ref_plane_key]

        else:
            if ref_plane_key == "xy":
                # Point was maybe already projected when added to the XYZ axo space
                new_point = self.plane.reference_planes[ref_plane_key].add_point(
                    Point(x=self.x, y=self.y),
                )
            elif ref_plane_key == "yz":
                # Point was maybe already projected when added to the XYZ axo space
                new_point = self.plane.reference_planes[ref_plane_key].add_point(
                    Point(y=self.y, z=self.z),
                )
            elif ref_plane_key == "zx":
                # Point was maybe already projected when added to the XYZ axo space
                new_point = self.plane.reference_planes[ref_plane_key].add_point(
                    Point(x=self.x, z=self.z),
                )

            # draw new projection line
            self.plane.drawing.add_compas_geometry(
                [CLine(self.data, new_point.data)],
            )
            self.projections[ref_plane_key] = new_point
            new_point.projections["xyz"].append(self)

        return new_point

    @property
    def __data__(self) -> list:
        """Give access to data in order to be used with compas methods.

        .. warning::

            The data is very different from the user defined values.
            They are all compas.geometry objects with only (X,Y)
            coordinates, all in the same plane (i.e. your piece of
            paper).

        """
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
        if (not isinstance(other, type(self))) or (self is None or other is None):
            # if the other item of comparison is not also of the Point class
            return False
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


def is_coplanar(points: list[Point]) -> bool:
    """Check if a series of points are in the same plane."""
    keys = [point.key for point in points]
    return len(set(keys)) == 1


def copy_point(point: Point) -> Point:
    if point.x:
        pass
    return Point()
