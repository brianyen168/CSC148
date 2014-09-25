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

    def test_get_leader_fails(self):
        with self.assertRaises(ShortChainError):
            self.empty_chain.get_leader()

    def test_get_second_simple(self):
        self.assertEqual(self.chain.get_second(), 'Janna')

    def test_get_second_fails(self):
        with self.assertRaises(ShortChainError):
            self.one_chain.get_second()

    def test_get_third_simple(self):
        self.assertEqual(self.chain.get_third(), 'Kevan')
        
    def test_get_third_fails(self):
        with self.assertRaises(ShortChainError):
            self.two_chain.get_third()

    def test_get_nth_simple(self):
        self.assertEqual(self.chain.get_nth(3), 'Kevan')

    def test_get_nth_fails(self):
        with self.assertRaises(ShortChainError):
            self.two_chain.get_nth(30)

if __name__ == '__main__':
    unittest.main(exit=False)
