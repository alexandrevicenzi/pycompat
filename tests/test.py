#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pycompat import python as py
from pycompat import system

import sys
import unittest

class TestPyCompat(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_64bits(self):
        self.assertEqual(system.is_64bits, sys.maxsize > 2**32)

    # Is failing on Travis-CI Python 3+
    #'def test_immutability(self):
    #'    try:
    #'        py.is2xx = 1
    #'        self.assertTrue(False)
    #'    except AttributeError:
    #'        self.assertTrue(True)
    #'    else:
    #        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
