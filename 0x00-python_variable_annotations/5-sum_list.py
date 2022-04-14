#!/usr/bin/env python3
"""
list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    type-annotated function sum_list
    """
    sum_: float = 0.0
    for num in input_list:
        sum_ += num
    return sum_
