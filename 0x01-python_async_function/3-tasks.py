#!/usr/bin/env python3
""" This module defines a python function """
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
