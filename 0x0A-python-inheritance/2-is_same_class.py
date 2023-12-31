#!/usr/bin/python3


"""A module that check for class similarity"""


def is_same_class(obj, a_class):
    """Using type() function to check for class similarity"""
    if type(obj) is a_class:
        return True
    else:
        return False
