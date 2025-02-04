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
