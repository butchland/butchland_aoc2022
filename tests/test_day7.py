import pytest
from butchland_aoc2022.day7 import *

@pytest.mark.parametrize(
    "test_input, expected", [
        ("$ cd /", ("cd", "/")), 
        ("$ ls", ("ls",)), 
        ("dir a", ("dir", "a")), 
        ("148448514 b.txt", ("size",148_448_514,"b.txt"))
])
def test_parse_line(test_input, expected):
    assert parse_line(test_input) == expected

