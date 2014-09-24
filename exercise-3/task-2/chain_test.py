# Exercise 3, Task 2 TESTS
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Exercise 3, Task 2 TESTS.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests,
and to be confident your code is correct!
"""
import unittest
from chain import PeopleChain, ShortChainError


class TestPeopleChain(unittest.TestCase):

    def setUp(self):
        self.chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        self.empty_chain = PeopleChain([])
        self.one_chain = PeopleChain(['David'])
        self.two_chain = PeopleChain(['Karen', 'Paul'])

    def test_get_leader_simple(self):
        self.assertEqual(self.chain.get_leader(), 'Iron Man')

    def test_get_second_simple(self):
        self.assertEqual(self.chain.get_second(), 'Janna')

    def test_get_third_simple(self):
        self.assertEqual(self.chain.get_third(), 'Kevan')

    def test_get_nth_simple(self):
        self.assertEqual(self.chain.get_nth(1), 'Janna')

    def test_raises_small_stack_error(self):
        with self.assertRaises(ShortChainError):
            self.chain.get_nth(200)

if __name__ == '__main__':
    unittest.main(exit=False)