#!/usr/bin/python3


"""The square module"""


class Square:
    """Defining the instance"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, space):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(x > 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = space

    def area(self):
        return self.__size**2

    def my_print(self):
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]

            print("")
        if self.__size == 0:
            print("")
