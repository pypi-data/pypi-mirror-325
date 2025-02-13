# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import unittest
from unittest.mock import patch

from axonometry import Axonometry, Line, Point, config

config.logger.setLevel(logging.INFO)

class TestAxonometryLines(unittest.TestCase):

    def setUp(self):
        self.axo = Axonometry(*config.random_valid_angles())
        self.line_xy = Line(Point(x=4, y=43), Point(x=19, y=24))
        self.line_xyz = Line(Point(x=16, y=25, z=20), Point(x=37, y=35, z=42))

    def test_adding_lines(self):
        self.axo.reference_planes['xy'].add_line(self.line_xy)
        self.axo.add_line(self.line_xyz)

@patch("axonometry.Axonometry.save_svg")
def test_saving_svg(self, mock_save_svg):
    svg_file = f"test_axo_{self.alpha}-{self.beta}.svg"
    """Test saving an Axonometry instance to a SVG file."""
    self.axo.save_svg(svg_file)
    mock_save_svg.assert_called_once_with(svg_file)

@patch("axonometry.Axonometry.show_paths")
def test_display_result(self, mock_show):
    self.axo.show_paths()
    mock_show.assert_called_once()
