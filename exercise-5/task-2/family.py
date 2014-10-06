# Exercise 5 - Family Tree
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# Connor Peet, 1001088208
#
# ---------------------------------------------


class Person:
    """Person class.

    Attributes:
    - name (str): The name of this Person
    - children (list of Person): a list of the Person objects who
                                 are the children of this Person
    """

    def __init__(self, name):
        """ (Person, str) -> NoneType

        Create a new Person object with the given name,
        and no children.
        """
        self.name = name
        self.children = []

    def count_descendants(self):
        """ (Person) -> int
        Return the number of descendants of self.
        """
        output = 0
        for child in self.children:
            output += 1 + child.count_descendants()

        return output