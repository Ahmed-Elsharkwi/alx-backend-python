#!/usr/bin/env python3
""" return the wating time of the wait function """
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ return the waiting time which is float """
    st = time.time()

    asyncio.run(wait_n(n, max_delay))

    et = time.time()

    return (et - st) / n
