#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns a list of True or False depending on divisibility by 2."""
    new_list = []

    for num in my_list:
        new_list.append(num % 2 == 0)

    return new_list
