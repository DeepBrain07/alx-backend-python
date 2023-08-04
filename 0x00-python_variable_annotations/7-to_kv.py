#!/usr/bin/env python3
""" This Module defines a python function """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    return (k, float(v**2))
