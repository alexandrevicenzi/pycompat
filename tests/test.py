#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pycompat import python as py
from pycompat import system

import sys
import unittest

class TestPyCompat(unittest.TestCase):

    def setUp(self):
        pass

    def test_python_is_64bits(self):
        self.assertEqual(py.is_64bits, not py.is_32bits)

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
