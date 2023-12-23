#!/usr/bin/python3


"""
defines an addition integer function
The function takes two arguments.
The second argument is optional. it is provided by default
"""


def add_integer(a, b=98):
    """
    It raises a TypeError if either of the arguments are non-integer or non-float
    a and b are casted to integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
