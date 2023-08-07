#!/usr/bin/env python3
""" This module defines a python function """
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """ This function returns a float """
    return sum(asyncio.run(wait_n(n, max_delay))) / n
