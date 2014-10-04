#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# These tests run only under Linux and Python 2.x +
# This is the Travis CI environment.
#

from pycompat import python as py
from pycompat import system

import sys
import unittest

class TestPyCompat(unittest.TestCase):

    def setUp(self):
        pass

    def test_python_is_64bits(self):
        self.assertEqual(py.is_64bits, not py.is_32bits)

    def test_is_cpython(self):
        self.assertEqual(py.is_cpython, not py.is_pypy)

    # Is failing on Travis-CI Python 3+
    #'def test_immutability(self):
    #'    try:
    #'        py.is2xx = 1
    #'        self.assertTrue(False)
    #'    except AttributeError:
    #'        self.assertTrue(True)
    #'    else:
    #        self.assertTrue(False)

    def test_python_is1xx(self):
        self.assertFalse(py.is1xx)

    def test_python_is2xx(self):
        self.assertEqual(py.is2xx, sys.version_info[0] == 2)

    def test_python_is3xx(self):
        self.assertEqual(py.is3xx, sys.version_info[0] == 3)

    def test_python_is_eqx(self):
        self.assertTrue(py.is_eq(sys.version_info[0]))

    def test_python_is_eqxx(self):
        self.assertTrue(py.is_eq(sys.version_info[0], sys.version_info[1]))

    def test_python_is_eqxxx(self):
        self.assertTrue(py.is_eq(sys.version_info[0], sys.version_info[1], sys.version_info[2]))

    def test_python_is_gtx(self):
        self.assertTrue(py.is_gt(sys.version_info[0] - 1))

    def test_python_is_gtxx(self):
        self.assertTrue(py.is_gt(sys.version_info[0], sys.version_info[1] - 1))

    def test_python_is_gtxxx(self):
        self.assertTrue(py.is_gt(sys.version_info[0], sys.version_info[1], sys.version_info[2] - 1))

    def test_python_is_ltx(self):
        self.assertTrue(py.is_lt(sys.version_info[0] + 1))

    def test_python_is_ltxx(self):
        self.assertTrue(py.is_lt(sys.version_info[0], sys.version_info[1] + 1))

    def test_python_is_ltxxx(self):
        self.assertTrue(py.is_lt(sys.version_info[0], sys.version_info[1], sys.version_info[2] + 1))

    def test_system_is_windows(self):
        self.assertFalse(system.is_windows)

    def test_system_is_cygwin(self):
        self.assertFalse(system.is_cygwin)

    def test_system_is_mac_os(self):
        self.assertFalse(system.is_mac_os)

    def test_system_is_linux(self):
        self.assertTrue(system.is_linux)


if __name__ == '__main__':
    unittest.main()
