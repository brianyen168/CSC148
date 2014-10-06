# Exercise 5, Task 1 TESTS
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Exercise 5, Task 1 TESTS.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests,
and to be confident your code is correct!
"""
import unittest
from list_map import LinkedListRec


class TestListMap(unittest.TestCase):

    def test_simple(self):
        names = LinkedListRec(['David', 'Jen', 'Paul'])
        lengths = names.map_f(len)
        self.assertEqual(lengths[0], 5)
        self.assertEqual(lengths[1], 3)
        self.assertEqual(lengths[2], 4)


if __name__ == '__main__':
    unittest.main(exit=False)