#!/usr/bin/python3


"""A module that sort elements in a list in ascending order"""


class List:
    """defining the constructor"""
    def __init__(self):
        self.Thelist = []

    def append(self, item):
        return self.Thelist.append(item)

    def __str__(self):
        return str(self.Thelist)

    def print_sorted(self):
        print(sorted(self.Thelist))


"""Defining a subclass to inherit from class List"""


class MyList(List):
    """Defining the subclass constructor"""
    def __init__(self):
        super().__init__()
