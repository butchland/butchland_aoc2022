__all__ = ["generate_totals", "sum_top_n"]


from typing import Generator
from fastcore.all import *


def generate_totals(
    input: list[str],  # list of strings each containing an int or empty line
) -> Generator[int, None, None]:
    """Generate totals
    from an input string
    consisting of lines
    where each line is an integer
    and delimited by an empty line
    """
    total = 0
    for line in input:
        if len(line) == 0:
            yield total
            total = 0
        else:
            total += int(line)

    yield total


def sum_top_n(
    input: list[str],  # list of strings each containing an int or empty line
    n: int,  # top n count
):
    """Sum top n of totals for the highest n totals"""
    max_n = L([0] * n)
    low_max = 0  # track lowest
    for total in generate_totals(input):
        if low_max < total:
            low_index = max_n.argfirst(lambda x: x == low_max)
            max_n[low_index] = total
            low_max = min(max_n)

    return sum(max_n)
