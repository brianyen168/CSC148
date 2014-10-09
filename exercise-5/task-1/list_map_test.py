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
from list_map import map_f


class TestListMap(unittest.TestCase):

    def test_multiple(self):
        names = LinkedListRec(['David', 'Jean', 'Paul'])
        lengths = map_f(names, len)
        self.assertEqual(lengths[0], 5)
        self.assertEqual(lengths[1], 4)
        self.assertEqual(lengths[2], 4)
        self.assertEqual(names[0], 'David')
        self.assertEqual(names[1], 'Jean')
        self.assertEqual(names[2], 'Paul')

    def test_empty(self):
        names = LinkedListRec([])
        lengths = map_f(names, len)
        self.assertEqual(lengths.is_empty(), True)



if __name__ == '__main__':
    unittest.main(exit=False)