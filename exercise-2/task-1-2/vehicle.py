# Exercise 2: Cars and Hover Cars
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# Connor Peet, 1001088208
#
# ---------------------------------------------
import math


class NotEnoughFuelError(Exception):
    pass


class Car:

    # Don't change this code!
    def __init__(self, fuel, efficiency):
        """ (Car, int, int) -> NoneType

        fuel is an int specifying the starting amount of fuel.
        efficiency is an int specifying how much fuel the car takes
        to travel 1 unit of distance.

        Initialize a new car with an amount of fuel and a fuel efficiency.
        The car's starting position is (0,0).
        """

        self.fuel = fuel
        self.efficiency = efficiency
        self.pos_x = 0
        self.pos_y = 0

    def _max_movement(self):
        """
        Returns the maximum distance which the car can move, with its
        current amount of fuel and efficiency.
        """
        return math.floor(self.fuel / self.efficiency)

    def _delta_to(self, new_x, new_y):
        """
        Returns the distance to the target x and y
        """
        return abs(new_x - self.pos_x) + abs(new_y - self.pos_y)

    def move(self, new_x, new_y):
        """ (Car, int, int) -> NoneType

        Move the car from its old position to (new_x, new_y).
        Reduce the car's fuel depending on its efficiency and how far it
        travelled.

        If there isn't enough fuel to reach (new_x, new_y),
        do not change car's position or fuel leve.
        Instead, raise NotEnoughFuelError.

        Remember that the car can only travel horizontally and vertically!
        """

        delta = self._delta_to(new_x, new_y)
        if delta > self._max_movement():
            raise NotEnoughFuelError('Not enough fuel to reach destination!')

        self.pos_x = new_x
        self.pos_y = new_y
        self.fuel -= self.efficiency * delta


class HoverCar(Car):

    hover_efficiency = 1 / 20

    def __init__(self, fuel, efficiency, hover_fuel):
        """ (HoverCar, int, int, int) -> NoneType

        hover_fuel is an int specifying the starting amount of hover fuel.

        Initialize a new HoverCar.
        """
        Car.__init__(self, fuel, efficiency)
        self.hover_fuel = hover_fuel

    def move(self, new_x, new_y):
        """ (HoverCar, int, int)

        Move the hover car according to the description in the exercise.
        Remember that hover cars try using regular fuel first,
        and only use hover fuel if there isn't enough regular fuel.

        Be sure to follow the implementation guidelines for full marks!
        """

        try:
            return Car.move(self, new_x, new_y)
        except NotEnoughFuelError as e:
            pass

        fuel_delta = math.sqrt((self.pos_x - new_x) ** 2 +(self.pos_y - new_y) ** 2) * self.hover_efficiency

        if self.hover_fuel < fuel_delta:
            raise NotEnoughFuelError('Not enough normal or hover fuel to reach destination!')

        self.pos_x = new_x
        self.pos_y = new_y
        self.hover_fuel -= math.ceil(fuel_delta)
