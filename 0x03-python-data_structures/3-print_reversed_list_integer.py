#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list = my_list[::-1]
    for i in list:
        print("{:d}".format(i))
