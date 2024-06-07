#!/usr/bin/env python3
"""
return sum_list which takes a list input_list of floats as argument and 
returns their sum as a float.
"""


def sum_list(input_list: float) -> float:
    """
    return sum_list
    """
    sum: float = 0.0

    for ele in input_list:
        sum += ele
    return sum
