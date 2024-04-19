#!/usr/bin/python3
"""testing MAX method"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """testing every case in max integer method"""
    def test_normal(self):
        """trying normal case"""
        self.assertEqual(max_integer([1, 2, 5]), 5)

    def test_no_args(self):
        """trying normal case"""
        self.assertEqual(max_integer(), None)

    def test_empty(self):
        """trying normal case"""
        self.assertEqual(max_integer([]), None)

    def test_first(self):
        """trying normal case"""
        self.assertEqual(max_integer([8, 2, 5]), 8)

    def test_mid(self):
        """trying normal case"""
        self.assertEqual(max_integer([1, 9, 5]), 9)

    def test_niga(self):
        """trying normal case"""
        self.assertEqual(max_integer([-1, 2, 5]), 5)

    def test_all_nega(self):
        """trying normal case"""
        self.assertEqual(max_integer([-1, -2, -5]), -1)

    def test_one(self):
        """trying normal case"""
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
