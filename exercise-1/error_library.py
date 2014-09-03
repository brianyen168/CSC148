# Exercise 1, Task 1: Runtime Errors
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# Connor Peet, 1001088208
#
# ---------------------------------------------
"""Exercise 1, Task 1: Runtime Errors."""


def bad_type():
    """When run, produces a TypeError."""
    "This isn't Javascript... " + 42


def bad_name():
    """When run, produces a NameError."""
    foo


def bad_attribute():
    """When run, produces an AttributeError."""
    'this is a bad'.attribute


def bad_index():
    """When run, produces an IndexError."""
    [][42]


def bad_key():
    """When run, produces a KeyError."""
    {}['bar']


def bad_zero():
    """When run, produces a ZeroDivisionError."""
    42 / 0


def bad_import():
    """When run, produces an ImportError."""
    import someSillyModule