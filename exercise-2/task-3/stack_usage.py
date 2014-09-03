# Exercise 2: Stack Preview
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# Connor Peet, 1001088208
#
# ---------------------------------------------

# This import will fail unless you've downloaded
# the stack.pyc file from the website
from stack import Stack


def remove_nth(stack, n):
    """
    Removes the nth item from the stack, and returns it.
    """
    saves = []
    for index in range(n - 1):
        saves.append(stack.pop())

    output = stack.pop()

    for saved in saves:
        stack.push(saved)

    return output


def remove_second(stack):
    """ (Stack) -> object

    Remove and return the second-highest item on stack.
    You may assume that stack always has at least two items.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(10)
    >>> stack.push(30)
    >>> stack.push(40)
    >>> remove_second(stack)
    30 # Second most recent element added
    >>> stack.pop()
    40 # Top element remains unchanged
    >>> stack.pop()
    10 # Next element is now 10; the 30 has been removed
    >>> stack.pop()
    1
    >>> stack.isempty()
    True
    """

    # YOUR CODE GOES HERE
    # HINT: this requires no more than a few lines of code.
    # If you're stuck, first try removing the top two elements.
    return remove_nth(stack, 2)
