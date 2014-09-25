# Exercise 3: More Stack Exercises
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# Connor Peet, 1001088208
#
# ---------------------------------------------
from stack import Stack
from stack import EmptyStackError


class SmallStackError(Exception):
    pass

def reverse_n(stack, count=None):
    """
    Reverses `count` items in the stack. If count is not given or None,
    the entire stack will be reversed.
    """

    items = []

    try:
        if count is None:
            while True: items.append(stack.pop())
        else:
            while count > 0:
                items.append(stack.pop())
                count -= 1

    except EmptyStackError:
        if count is not None:
            raise SmallStackError()
    finally:
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