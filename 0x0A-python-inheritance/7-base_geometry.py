#!/usr/bin/python3


"""A module that raise exceptions"""


class BaseGeometry:
    """Defining a public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
