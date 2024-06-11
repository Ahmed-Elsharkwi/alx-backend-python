#!/usr/bin/env python3
"""
get a random number and return it
"""
import random


async def wait_random(max_delay=10):
    """ return an float random number """
    return random.uniform(0, max_delay)
