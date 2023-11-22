#!/usr/bin/python3


"""The module of the square"""


class Square:
    """Defining the instance"""
    def __init__(self, size=0):
        """Using the private instance attribute"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2
