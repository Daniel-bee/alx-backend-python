#!/usr/bin/env python3
"""
mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    type-annotated function sum_mixed_list
    """
    sum_: float = 0.0
    for num in mxd_lst:
        sum_ += num
    return sum_
