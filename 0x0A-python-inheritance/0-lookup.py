#!/usr/bin/python3


"""A module that returns a list of attributes and methods of an object"""


def lookup(obj):
    print(list(dir(obj)))
