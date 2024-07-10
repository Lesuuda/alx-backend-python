#!/usr/bin/env python3
""" Async generator """


import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """ Async generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
