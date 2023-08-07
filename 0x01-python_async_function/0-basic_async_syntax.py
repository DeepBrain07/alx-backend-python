#!/usr/bin/env python3
""" This module defines a python function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ This function waits for a random delay between 0 and max_delay """
    randf = random.uniform(0, max_delay + 1)
    await asyncio.sleep(randf)
    return randf
