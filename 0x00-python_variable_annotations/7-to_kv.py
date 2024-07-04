#!/usr/bin/python3
"""
This module contains a function that takes a string k
and an int OR  float v and returns a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ This function returns a tuple """
    return (k, v * v)
