#!/usr/bin/env python3
""" This Module defines a python function """
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ This function  returns a function that
    multiplies a float by multiplier """
    def inner_multiplier(arg: float) -> float:
        return arg * multiplier
    return inner_multiplier
