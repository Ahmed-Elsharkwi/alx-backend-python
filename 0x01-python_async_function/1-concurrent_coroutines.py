#!/usr/bin/env python3
""" return list of number """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the dely time for each function """
    new_list = []

    for i in range(0, n):
        result = asyncio.create_task(wait_random(max_delay))
        delay = await result

        for idx in range(0, len(new_list)):
            if new_list[idx] > delay:
                temp = new_list[idx]
                new_list[idx] = delay
                delay = temp
        new_list.append(delay)

    return new_list
