#!/usr/bin/env python3
"""
get a random number and return it
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ return an float random number """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
