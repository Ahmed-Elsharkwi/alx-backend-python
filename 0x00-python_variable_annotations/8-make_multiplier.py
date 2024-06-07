#!/usr/bin/env python3
"""
return sum_list which takes a list input_list of floats as argument and
returns their sum as a float.
"""
from typing import List, Union, Tuple, Callable


def make_multiplier(k: float) -> Callable[[float], float]:
    """
    return function
    """
    def fun(n: float) -> float:
        """ return a float """
        return n * k
    return (fun)
