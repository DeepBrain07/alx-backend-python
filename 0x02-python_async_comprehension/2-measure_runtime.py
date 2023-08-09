#!/usr/bin/env python3
""" This module defines a python function """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ executes async_comprehension four times
    in parallel using asyncio.gather """
    s_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    elapsed_time = time.time() - s_time
    return elapsed_time
