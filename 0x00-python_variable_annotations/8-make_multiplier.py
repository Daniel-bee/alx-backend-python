#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier """
    def fn(n: float):
        return n * multiplier
    return fn
