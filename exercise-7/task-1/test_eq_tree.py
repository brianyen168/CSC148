# Exercise 7, Task 1 TESTS
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Exercise 7, Task 1 TESTS.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests,
and to be confident your code is correct!
"""
import unittest
from tree import Tree


class TestTreeEq(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(1)
        self.tree.subtrees = [Tree('Hi'), Tree(3)]

    def test_simple_eq(self):
        tree2 = Tree(1)
        tree2.subtrees = [Tree('Hi'), Tree(3)]
        self.assertTrue(self.tree == tree2)

    def test_order_matters(self):
        tree2 = Tree(1)
        tree2.subtrees = [Tree(3), Tree('Hi')]
        self.assertFalse(self.tree == tree2)

    def test_missing_item_not_equal(self):
        tree2 = Tree(1)
        tree2.subtrees = [Tree(3)]
        self.assertFalse(self.tree == tree2)

    def test_has_extra_not_equal(self):
        tree2 = Tree(1)
        tree2.subtrees = [Tree('Hi'), Tree(3)]
        tree2.subtrees[0].subtrees = [Tree(2)]
        self.assertFalse(self.tree == tree2)

    def test_empty_not_equal(self):
        tree2 = Tree(1)
        self.assertFalse(self.tree == tree2)

    def test_empty_equal(self):
        self.assertTrue(Tree(1) == Tree(1))

    def test_not_equal_to_stuff(self):
        self.assertFalse(Tree(1) == 0)


if __name__ == '__main__':
    unittest.main(exit=False)
