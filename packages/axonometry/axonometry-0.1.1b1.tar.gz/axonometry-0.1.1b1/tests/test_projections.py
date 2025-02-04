# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
from unittest.mock import patch
import logging

from axonometry import Axonometry, Point, config

config.logger.setLevel(logging.DEBUG)

class TestAxonometryProjections(unittest.TestCase):

    def setUp(self):
        self.alpha, self.beta = config.random_valid_angles()
        self.axo = Axonometry(self.alpha, self.beta)

        # Creates a XYZ point by 2 random computed auxilary projections
        self.p0 = self.axo.add_point(Point(x=15, y=15, z=30))
        # Project XYZ point on refernce planes. Existin points will not be created twice.
        _ = self.p0.project(ref_plane_key="xy")
        _ = self.p0.project(ref_plane_key="yz")
        _ = self.p0.project(ref_plane_key="zx")

        # Create point in XY reference plane
        self.p1 = self.axo["xy"].add_point(Point(x=30, y=20))
        # Project point into XYZ
        self.p1_axo = self.p1.project(distance=50)
        # Project on remaining reference planes
        self.p1_axo.project(ref_plane_key="yz")  # TODO: remove case were point is doubled c.f. next test case
        self.p1_axo.project(ref_plane_key="zx")  # idem

        self.p2 = self.axo["yz"].add_point(Point(y=1, z=15))
        self.p2_axo = self.p2.project(distance=25)
        self.p2_axo.project(ref_plane_key="xy")
        self.p2_axo.project(ref_plane_key="zx")

        self.p3 = self.axo["zx"].add_point(Point(z=5, x=10))
        self.p3_axo = self.p3.project(distance=15)
        self.p3_axo.project(ref_plane_key="xy")
        self.p3_axo.project(ref_plane_key="yz")

    def test_geoemtry_projection_data(self):
        """TODO: Check that points were not created double."""
        pass

    @patch("axonometry.Axonometry.save_svg")
    def test_saving_svg(self, mock_save_svg):
        svg_file = f"test_axo_{self.alpha}-{self.beta}.svg"
        """Test saving an Axonometry instance to a SVG file."""
        self.axo.save_svg(svg_file)
        mock_save_svg.assert_called_once_with(svg_file)

    @patch("axonometry.Axonometry.show")
    def test_display_result(self, mock_show):
        self.axo.show()
        mock_show.assert_called_once()


if __name__ == "__main__":
    unittest.main()
