"""The toolbox to script axonometric drawing operations."""

# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .axonometry import Axonometry
from .config import Config, config
from .drawing import Drawing
from .geometry import Line, Point, Surface
from .trihedron import Trihedron

__all__ = [
    "Axonometry",
    "Config",
    "Drawing",
    "Line",
    "Point",
    "Surface",
    "Trihedron",
    "config",
]
