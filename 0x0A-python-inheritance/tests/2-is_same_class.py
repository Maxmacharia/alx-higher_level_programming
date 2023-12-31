#!/usr/bin/python3


"""A module that checks for instances for specific classes"""


def is_same_class(obj, a_class):
    """Using the isinstance to check class similarity"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
