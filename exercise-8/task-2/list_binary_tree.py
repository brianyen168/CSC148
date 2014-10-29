# ListBinaryTree class
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


class ListBinaryTree:
    def __init__(self, items):
        """ (ListBinaryTree, list) -> NoneType

        Create a complete binary tree in list form
        with the specified items.

        The [None] is used to start indexing items at 1
        instead of 0, which is easier.
        """

        self.items = [None] + items

    def is_empty(self):
        """ (ListBinaryTree) -> bool

        Return True if self is empty.
        """
        return len(self.items) == 1

    def root(self):
        """ (ListBinaryTree) -> object

        Return the root item of the tree.
        If the tree is empty, raise IndexError.
        """

        if self.is_empty():
            raise IndexError
        else:
            return self.items[1]

    def go_down_greedy(self, index=1):
        """ (ListBinaryTree) -> list

        Return a list of items starting at the node with position index
        and ending at a leaf, where at each level the child node
        with the smaller value is chosen to recurse on
        (in case of ties, choose the left child).

        By default, the list starts at the root of the tree.

        Note: you may use either the provided subtree methods,
        or do the index arithmetic yourself.
        For maximum learning, try both!
        """
        output = [self.items[index]]

        left = self.left(index)
        right = self.right(index)

        if len(self.items) <= left:
            return output
        if len(self.items) <= right:
            return output + self.go_down_greedy(left)

        if self.items[right] < self.items[left]:
            return output + self.go_down_greedy(right)
        else:
            return output + self.go_down_greedy(left)

    # Index helper functions
    def left(self, index):
        """ (int) -> int

        Return the index of the left child of the node as position index.
        """
        return 2 * index

    def right(self, index):
        """ (int) -> int

        Return the index of the right child of the node as position index.
        """
        return 2 * index + 1
