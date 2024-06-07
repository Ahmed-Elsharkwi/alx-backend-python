#!/usr/bin/env python3
"""
return sum_list which takes a list input_list of floats as argument and
returns their sum as a float.
"""
from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    """
    return mxd_lst
    """
    sum = 0.0

    for ele in mxd_lst:
        sum += ele
    return sum
