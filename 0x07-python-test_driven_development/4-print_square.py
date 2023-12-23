#!/usr/bin/python3


"""A square module"""


def print_square(size):
    """
    if size is not an integer raise TypeError
    if size is less than 0 raise TypeError
    if size is a float and is less than o raise TypeError
    The square is printed in a loop using #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    result = ""
    for i in range(size):
        result = result + "#" * size + "\n"
    print(result)
    return result.rstrip("\n")
