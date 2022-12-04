import pytest
from butchland_aoc2022.day4 import *


@pytest.fixture()
def samples():
    yield """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()


def test_get_range():
    assert get_range("2-4") == range(2, 4)


def test_assign_ranges():
    assert get_assign_ranges("2-4,6-8") == [range(2, 4), range(6, 8)]


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((range(2, 4), range(6, 8)), False),
        ((range(2, 8), range(3, 7)), True),
        ((range(6, 6), range(4, 6)), False),
        ((range(2, 6), range(4, 8)), False),
    ],
)
def test_contains(test_input, expected):
    assert contains(*test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((range(2, 4), range(6, 8)), False),
        ((range(2, 8), range(3, 7)), True),
        ((range(6, 6), range(4, 6)), True),
        ((range(2, 6), range(4, 8)), False),
    ],
)
def test_contains_each_other(test_input, expected):
    assert contains_each_other(*test_input) == expected

def test_get_overlapping(samples):
    overlapping = get_overlapping(samples)
    assert len(overlapping) == 2

@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((range(2, 4), range(6, 8)), False),
        ((range(2, 8), range(3, 7)), True),
        ((range(6, 6), range(4, 6)), True),
        ((range(2, 6), range(4, 8)), True),
        ((range(2, 10), range(4, 8)), True),
        ((range(4, 8), range(2, 10)), False),
    ],
)
def test_partly_contains(test_input, expected):
    assert partly_contains(*test_input) == expected

@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((range(2, 4), range(6, 8)), False),
        ((range(2, 8), range(3, 7)), True),
        ((range(6, 6), range(4, 6)), True),
        ((range(2, 6), range(4, 8)), True),
        ((range(2, 10), range(4, 8)), True),
        ((range(4, 8), range(2, 10)), True),

    ],
)
def test_partly_or_fully_contains_each_other(test_input, expected):
    assert partly_or_fully_contains_each_other(*test_input) == expected

def test_get_partly_overlapping(samples):
    overlapping = get_partly_overlapping(samples)
    assert len(overlapping) == 4
