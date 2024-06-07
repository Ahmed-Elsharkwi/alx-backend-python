#!/usr/bin/env python3
"""
return sum_list which takes a list input_list of floats
"""
from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return list """
    return [(i, len(i)) for i in lst]
