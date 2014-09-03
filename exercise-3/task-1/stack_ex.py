# Exercise 3: More Stack Exercises
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <full name>, <utorid>
#
# ---------------------------------------------
from stack import Stack
# from stack import EmptyStackError


class SmallStackError(Exception):
    pass


def reverse_n(stack, n=None):
    """
    Reverses `n` items in the stack. If n is not given or None, the entire
    stack will be reversed.
    """
    if n is None:
        count = float('inf')
    else:
        count = n

    items = []

    try:
        while count > 0:
            items.append(stack.pop())
            count -= 1

    except IndexError as e:
        if n is not None:
            raise SmallStackError()

    for item in items:
        stack.push(item)


def reverse_top_two(stack):
    """ (Stack) -> NoneType

    Reverse the top two elements on stack.
    Raise a SmallStackError if stack has fewer than two elements.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse_top_two(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    reverse_n(stack, 2)


def reverse(stack):
    """ (Stack) -> NoneType

    Reverse all the elements of stack.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    reverse_n(stack)