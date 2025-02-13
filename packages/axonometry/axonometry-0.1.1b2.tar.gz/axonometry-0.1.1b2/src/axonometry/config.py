"""Settings class."""

# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import pathlib
import random


class Config:
    """Settings in the form of a class.

    A Config instance is beeing initiated on import::

        from aonometry import config

    DINA paper sizes are accessed from a dictionnary::

        config.din["A1"]["landscape"]
        config.din["A3"]["portrait"]

    Save log messages::

        config.logger.info("some message.")
    """

    def __init__(self) -> None:  # noqa: D107
        self.css_pixel = 3.7795275591
        self.din: dict = {
            "A1": {
                "portrait": (594 * self.css_pixel, 841 * self.css_pixel),
                "landscape": (841 * self.css_pixel, 594 * self.css_pixel),
            },
        }  #: Dictionnary of standard page sizes.
        self.logger: logging.Logger = logging.getLogger(__name__)  #:
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler("output/debug.log")
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def random_valid_angles(self) -> tuple:
        """Compute an angle pair which can produce a valid axonometric drawing.

        The notation follows standard hand-drawn axonometry conventions expressed as a tuple of
        the two angles between the X and Y from the "axonoemtric horizon".

        TODO: allow a zero angle value.

        """
        alpha = random.choice(list(range(91)))  # noqa: S311
        beta = random.choice(list(range(91)))  # noqa: S311
        while not self.is_valid_angles((alpha, beta)):
            alpha = random.choice(list(range(91)))  # noqa: S311
            beta = random.choice(list(range(91)))  # noqa: S311

        return (alpha, beta)

    def is_valid_angles(self, angles: tuple) -> bool:
        """Test if an angle pair are valid axonometry angles.

        Check if angles satisfy the following conditions::

            not (180 - (alpha + beta) >= 90 and
            not (alpha == 0 and beta == 0) and
            not (alpha == 90 and beta == 0) and
            not (alpha == 0 and beta == 90)

        .. hint::

            Currently the angle value 0 is not supported.
            But one can use a float vlue of .1 to approximate zero.
        """
        return (
            180 - (angles[0] + angles[1]) >= 90
            and not (angles[0] == 0 and angles[1] == 0)
            and not (angles[0] == 90 and angles[1] == 0)
            and not (angles[0] == 0 and angles[1] == 90)
        )


pathlib.Path("output/").mkdir(parents=True, exist_ok=True)
config = Config()

# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Trying to funnel the compas Line and Polyline through shapely into vpype.
I guess the only compas objects in question are Line, Polyline and eventually
Point (becoming very small circles I guess).

References:
    https://compas.dev/compas/latest/api/generated/compas.geometry.Line.html
    https://shapely.readthedocs.io/en/latest/reference/shapely.LineString.html#shapely.LineString
    https://vpype.readthedocs.io/en/latest/api/vpype.LineCollection.html#vpype.LineCollection.append
"""

# from compas.geometry import Line, Polyline
# from vpype import Document, LineCollection
# from vpype_cli import execute


# def convert_compas_to_shapely(compas_geometry):
#     """Convert a Compas geometry object to a Shapely LineString."""
#     from shapely import LineString

#     if isinstance(compas_geometry, Line):
#         return LineString(
#             [
#                 (compas_geometry.start.x, compas_geometry.start.y),
#                 (compas_geometry.end.x, compas_geometry.end.y),
#             ]
#         )
#     elif isinstance(compas_geometry, Polyline):
#         return LineString([(point.x, point.y) for point in compas_geometry])
#     else:
#         raise ValueError("Unsupported Compas geometry type")


# def convert_compas_to_vpype_lines(compas_geometries):
#     """Convert a list of Compas geometries to a vpype LineCollection."""
#     vpype_lines = LineCollection()
#     for compas_geometry in compas_geometries:
#         shapely_line = convert_compas_to_shapely(compas_geometry)
#         vpype_lines.append(shapely_line)
#     return vpype_lines


# def create_vpype_document(compas_geometries):
#     """Create a vpype Document from a list of Compas geometries."""
#     layers = convert_compas_to_vpype_lines(compas_geometries)
#     document = Document()
#     for layer in layers:
#         document.add(layer, layer_id=1)  # Assuming all lines are on the same layer
#     return document


# # Example usage
# compas_single_line = Line((100, 100), (200, 200))
# compas_polyline = Polyline([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)])

# # Create a vpype document from Compas geometries
# document = create_vpype_document([compas_single_line, compas_polyline])

# # Display the document with VPype CLI
# execute("show --colorful", document=document)
