#!/usr/bin/env python3
"""
first element of a sequence
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    correct duck-typed annotations
    """
    if lst:
        return lst[0]
    return None
    