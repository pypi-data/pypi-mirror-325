# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

from compas.geometry import Line as CLine

from .point import Point, is_coplanar


class Line:
    """To be implemented soon."""

    def __init__(self, start: Point, end: Point) -> None:  # noqa: D107
        assert is_coplanar([start, end]), "Points are not in the same plane."
        self.plane = None  # set by parent
        self.projections = {"xy": None, "yz": None, "zx": None, "xyz": []}
        self.start = start
        self.end = end
        self.key = {start.key, end.key}.pop()
        self.data: CLine | None = None

    @property
    def __data__(self):
        return {"start": self.start.data.__data__, "end": self.end.data.__data__}
