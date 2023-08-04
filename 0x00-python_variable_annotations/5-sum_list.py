#!/usr/bin/env python3
""" This Module defines a python function """
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ This function returns the sum of a list """
    sum: float = 0
    for x in input_list:
        sum += x
    return sum
