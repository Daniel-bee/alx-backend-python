#!/usr/bin/env python3
"""
Type Checking
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Type Checking
    """
    if lst:
        return lst[0]
    return None
