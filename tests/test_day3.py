import pytest
from butchland_aoc2022.day3 import *


@pytest.fixture()
def sample_input():
    yield """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split(
        "\n"
    )  # type: ignore


def test_common_item(sample_input):
    assert common_item(sample_input[0]) == "p"
    assert common_item(sample_input[1]) == "L"
    assert common_item(sample_input[2]) == "P"
    assert common_item(sample_input[3]) == "v"
    assert common_item(sample_input[4]) == "t"
    assert common_item(sample_input[5]) == "s"


@pytest.mark.parametrize(
    "test_input, expected", [("p", 16), ("a", 1), ("A", 27), ("Z", 52)]
)
def test_priority(test_input, expected):
    assert priority(test_input) == expected


def test_sum_priorities(sample_input):
    assert sum_priorities(sample_input) == 157


def test_get_group(sample_input):
    groups = list(generate_group(sample_input))
    assert len(groups) == 2
    assert len(groups[0]) == 3
    assert len(groups[1]) == 3


def test_find_group_badge(sample_input):
    groups = list(generate_group(sample_input))
    assert find_group_badge(groups[0]) == "r"
    assert find_group_badge(groups[1]) == "Z"


def test_sum_badge_priorities(sample_input):
    assert sum_badge_priorities(sample_input) == 70
