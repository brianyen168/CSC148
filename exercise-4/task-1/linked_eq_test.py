# Exercise 4, Task 1 TESTS
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Exercise 4, Task 1 TESTS.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests,
and to be confident your code is correct!
"""
import unittest
from linked_list import LinkedList


class TestLinkedListEq(unittest.TestCase):

    def test_simple(self):
        list1 = LinkedList([1])
        list2 = LinkedList([1])

        self.assertTrue(list1 == list2)
        self.assertTrue(list1.__eq__(list2))

    def test_simple_multiple(self):
        list1 = LinkedList([1, 2])
        list2 = LinkedList([1, 2])

        self.assertTrue(list1 == list2)
        self.assertTrue(list2 == list1)

    def test_fails_on_extraneous(self):
        list1 = LinkedList([1, 2])
        list2 = LinkedList([1])

        self.assertFalse(list1 == list2)
        self.assertFalse(list2 == list1)

    def test_equal_empty_lists(self):
        list1 = LinkedList([])
        list2 = LinkedList([])

        self.assertTrue(list1 == list2)
        self.assertTrue(list2 == list1)

    def test_compares_with_empty_lists(self):
        list1 = LinkedList([2])
        list2 = LinkedList([])

        self.assertFalse(list1 == list2)
        self.assertFalse(list2 == list1)

    def test_fails_if_out_of_order(self):
        list1 = LinkedList([1, 2])
        list2 = LinkedList([2, 1])

        self.assertFalse(list1 == list2)
        self.assertFalse(list2 == list1)



if __name__ == '__main__':
    unittest.main(exit=False)