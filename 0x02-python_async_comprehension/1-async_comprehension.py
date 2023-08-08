#!/usr/bin/env python3
""" This module defines a python function """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ This function returns 10 random numbers """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
