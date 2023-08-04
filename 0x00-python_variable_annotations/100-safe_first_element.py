#!/usr/bin/env python3
""" This Module defines a python function """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ This is a augmented function """
    if lst:
        return lst[0]
    else:
        return None
