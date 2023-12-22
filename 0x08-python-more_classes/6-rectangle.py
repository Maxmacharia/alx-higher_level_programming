#!/usr/bin/python3


"""A rectangle module"""


class Rectangle:
    number_of_instances = 0
    """Defining an instanse"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (2 * self.__width) + (2 * self.__height)
        if self.__width == 0 or self.__height == 0:
            return 0

    def __str__(self):
        result = ""
        for i in range(self.__height):
            result = result + "#" * self.__width + "\n"
        return result.rstrip("\n")
        if self.__width == 0 or self.__height == 0:
            print()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def get_number_of_instances(cls):
        return cls.number_of_instances