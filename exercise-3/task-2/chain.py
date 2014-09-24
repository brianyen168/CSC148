# Exercise 3: PeopleChain
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# Connor Peet, 1001088208
#
# ---------------------------------------------
"""Exercise 3, Task 2: PeopleChain.

Person: a person in the chain.
PeopleChain: ordered chain consisting of people.
ShortChainError: indicates chain is too short to perform action.
"""


class ShortChainError(Exception):
    pass


class Person:
    def __init__(self, name):
        """ (Person, str) -> NoneType

        Create a person who is initially not only onto anyone.
        """
        self.name = name
        self.next = None  # Initially holding onto no one


class PeopleChain:
    def __init__(self, names):
        """ (Person, list of str) -> NoneType

        Create Person objects linked together in the order provided in names.
        Set the leader of the chain as the first person in names.
        """

        if len(names) == 0:
            # No leader, representing an empty chain!
            self.leader = None
        else:
            # Set leader
            self.leader = Person(names[0])
            current_person = self.leader
            for name in names[1:]:
                # Set the link for the current person
                current_person.next = Person(name)
                # Update the current person
                # Note that current_person always refers to
                # the LAST person in the chain
                current_person = current_person.next

    def get_leader(self):
        """ (Person) -> str

        Return the name of the leader of the chain.
        Raise ShortChainError if chain has no leader.
        """
        return self.get_nth(0)

    def get_second(self):
        """ (Person) -> str

        Return the name of the second person in the chain,
        i.e., the one the leader is holding onto.
        Raise ShortChainError if chain has no second person.
        """
        return self.get_nth(1)

    def get_third(self):
        """ (Person) -> str

        Return the name of the third person in the chain.
        Raise ShortChainError if chain has no third person.
        """
        return self.get_nth(2)

    def get_nth(self, n):
        """ (Person) -> str

        Precondition: n >= 1

        Return the name of the n-th person in the chain.
        Raise ShortChainError if chain doesn't have n people.

        Remember: you must use a for or while loop in this function body!!
        """
        if self.leader is None:
            raise ShortChainError('This chain has no people!')

        person = self.leader

        for i in range(n):
            person = person.next
            if person is None:
                raise ShortChainError()

        return person.name