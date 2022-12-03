from butchland_aoc2022.day1 import *


def test_generate_totals():
    input = ["1", "", "2", "", "3", "", "4"]
    result = list(generate_totals(input))
    assert result == [1, 2, 3, 4]


def test_sum_top_n():
    input = ["1", "", "2", "", "3", "", "4"]
    result = sum_top_n(input, 3)
    assert result == 2 + 3 + 4
