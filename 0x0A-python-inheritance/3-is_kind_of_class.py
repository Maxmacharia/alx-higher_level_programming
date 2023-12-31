#!/usr/bin/python3


"""A module that check for class similarity"""


def is_kind_of_class(obj, a_class):
    """Using isinstance to check for class similarity"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
