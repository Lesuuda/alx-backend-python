#!/usr/bin/env python3
"""
contains a function that takes a list of floats and returns
their sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns the sum of a list of floats """
    return sum(mxd_lst)
