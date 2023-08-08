#!/usr/bin/env python3
""" This module defines a python function """
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """ This function spawns wait_random n times
    with the specified max_delay """
    lst = []
    lst2 = []
    for _ in range(n):
        lst.append(task_wait_random(max_delay))
    for e in asyncio.as_completed(lst):
        lst2.append(await e)
    return lst2
