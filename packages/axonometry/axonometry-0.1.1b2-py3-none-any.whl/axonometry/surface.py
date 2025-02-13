# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later


class Surface:
    """To be implemented soon."""

    def __init__(self):  # noqa: D107
        self.plane = None  # set by parent
        self.projections = {"xy": None, "yz": None, "zx": None, "xyz": []}
