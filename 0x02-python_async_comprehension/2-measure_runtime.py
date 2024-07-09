#!/usr/bin/env python3
"""" Measure runtime"""

import asyncio
import time


async_comprenhension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure runtime """
    start_time = time.time()
    await asyncio.gather(*(async_comprenhension() for _ in range(4)))
    return time.time() - start_time
