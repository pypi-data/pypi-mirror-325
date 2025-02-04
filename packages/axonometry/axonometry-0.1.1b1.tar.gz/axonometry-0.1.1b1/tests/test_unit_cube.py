# SPDX-FileCopyrightText: 2024 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
import logging
from axonometry import config

config.logger.setLevel(logging.DEBUG)


class TestAxonometryAngles(unittest.TestCase):

    def test_manual_unit_cube(self):
        pass


if __name__ == "__main__":
    unittest.main()
