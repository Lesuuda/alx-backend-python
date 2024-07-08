#!/usr/bin/env python3
"""
executes multiple coroutines at the same time with async
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """executes multiple coroutines at the same time with async"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
