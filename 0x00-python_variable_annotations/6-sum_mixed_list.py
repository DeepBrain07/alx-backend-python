#!/usr/bin/env python3
""" This Module defines a python function """
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """ This function returns the sum of a list """
    sum: float = 0
    for x in mxd_lst:
        sum += x
    return sum
