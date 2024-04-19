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


if __name__ == '__main__':
    unittest.main()
