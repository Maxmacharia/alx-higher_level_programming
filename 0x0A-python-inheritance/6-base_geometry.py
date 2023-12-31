#!/usr/bin/python3



"""A module that raise an exeception"""


class BaseGeometry:
    """Defining a public attribute instance"""
    def area(self):
        raise Exception("area() is not implemented")
