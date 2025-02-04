"""Main object to start drawing."""
# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import math
import pathlib

from .config import config
from .drawing import Drawing
from .geometry import Plane, ReferencePlane
from .trihedron import Trihedron


class Axonometry(Plane):
    """Represents an axonometric projection with given angles.

    Not mouch operations happen on this level, this class is more
    like a collection from which to access Trihedron and ReferencePlane
    objects. But this class also inherits Plane, therefore can be used
    as well to add geometries to the Drawing instance.

    .. note::

        When adding objects, and they have only two of the x y z, it means they are projecitons
        in a reference plane.

    """

    def __init__(  # noqa: D107
        self,
        *angles: tuple,
        trihedron_position: tuple = (0, 0),
        ref_planes_distance: float = 100.0,
        trihedron_size: float = 100.0,
    ) -> None:
        super().__init__()  # Call the parent class constructor if necessary
        # self.__angles = tuple(angles)
        self.drawing = Drawing()  #: The wrapped object
        self.key = "xyz"
        config.logger.info(f"[START] Axonometry {angles[0]}°/{angles[1]}°")
        self.trihedron = Trihedron(
            tuple(angles),
            position=trihedron_position,
            size=trihedron_size,
            ref_planes_distance=ref_planes_distance,
        )
        self.reference_planes = self.trihedron.reference_planes
        for plane in self.reference_planes.values():
            plane.axo = self  # necessary to evaluate the geometry objects' membership
            plane.drawing = self.drawing  # necessary to draw in plane
            # plane.update_matrix()
        # Add Trihedron to Drawing
        self.drawing.add_compas_geometry(self.trihedron.axes.values())
        for plane in self.reference_planes.values():
            self.drawing.add_compas_geometry(plane.axes)

    def show(self) -> None:
        """Display drawing."""
        self.drawing.show()

    def save_svg(self, filename: str, directory: str = "./output/") -> None:
        """Save drawing to file.

        TODO: check best pracatice for file location.

        :param filename: Name of the SVG file.
        :param directory: Path to directory, defaults to ``./output/``.
        """
        try:
            with pathlib.Path.open(directory + filename, "w") as f:
                self.drawing.save_svg(f)
        except FileExistsError:
            config.logger.info("Already exists.")

    def __repr__(self) -> str:
        """Get axonometry values in standard horizon angle notation."""
        return f"Axonometry {math.degrees(self.trihedron.axo_angles[0])}°/{math.degrees(self.trihedron.axo_angles[1])}°"

    def __getitem__(self, item) -> ReferencePlane:
        """Select a reference plane by key."""
        if item in self.reference_planes:
            return self.reference_planes[item]
        return self
