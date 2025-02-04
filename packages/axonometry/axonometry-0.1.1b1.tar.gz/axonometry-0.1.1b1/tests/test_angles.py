# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
import logging
from axonometry import Axonometry, config

config.logger.setLevel(logging.DEBUG)

class TestAxonometryAngles(unittest.TestCase):

    def test_angles(self):
        """Test creating Axonometry instances with series of angles."""
        for alpha in range(0, 91):
            for beta in range(0, 91):
                if config.is_valid_angles((alpha, beta)):
                    """Test with valid angle pair."""
                    ax = Axonometry(alpha, beta)
                    self.assertIsNotNone(ax, f"Failed with alpha={alpha}, beta={beta}")
                else:
                    """Test with invalid angle pair."""
                    with self.assertRaises(
                        AssertionError,
                        msg=f"Accepted invalid angle pair (alpha={alpha}, beta={beta}",
                    ):
                        Axonometry(alpha, beta)


if __name__ == "__main__":
    unittest.main()
