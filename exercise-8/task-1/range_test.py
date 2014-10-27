# Exercise 8, Task 1 TESTS
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Exercise 8, Task 1 TESTS.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests,
and to be confident your code is correct!
"""
import unittest
from bst import BinarySearchTree


class TestRange(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree(5)
        # Notice that we're using the interface method
        # to add values to the tree, rather than
        # manipulating the left and right attributes directly.
        self.bst.insert(5)
        self.bst.insert(10)
        self.bst.insert(15)
        self.bst.insert(20)
        self.bst.insert(25)
        self.bst.insert(30)
        self.bst.insert(30)

    def test_simple(self):
        self.assertEqual(self.bst.list_range(4, 7), [5, 5])
        self.assertEqual(self.bst.list_range(12, 50), [15, 20, 25, 30, 30])

    def test_inclusive(self):
        self.assertEqual(self.bst.list_range(5, 15), [5, 5, 10, 15])
        self.assertEqual(self.bst.list_range(25, 30), [25, 30, 30])

    def test_simple_empty(self):
        self.assertEqual(self.bst.list_range(6, 7), [])


if __name__ == '__main__':
    unittest.main(exit=False)
