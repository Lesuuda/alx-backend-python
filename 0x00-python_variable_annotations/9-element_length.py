#!/usr/bin/python3
"""
This module contains a function that calculates the length of a list
"""


from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function calculates the length of a list """
    return [(i, len(i)) for i in lst]
