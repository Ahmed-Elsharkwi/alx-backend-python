#!/usr/bin/env python3
"""
measure time
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure time """
    st = time.time()
    coros = [async_comprehension() for i in range(4)]
    await asyncio.gather(*coros)
    et = time.time()
    return et - st
