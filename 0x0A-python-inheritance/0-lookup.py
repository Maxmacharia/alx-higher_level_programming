#!/usr/bin/python3


"""A module that returns a list of attributes and methods of an object"""


def lookup(obj):
    """This prints all attributes and methods of an object in a list"""
    return list(dir(obj))
