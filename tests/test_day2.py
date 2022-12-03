import pytest
from butchland_aoc2022.day2 import *

@pytest.mark.parametrize("test_input,expected", [
        (("Paper","Rock"), 6),
        (("Paper","Scissors"), 0),
        (("Rock","Scissors"), 6),
        (("Rock","Paper"), 0),
        (("Scissors","Paper"), 6),
        (("Scissors","Rock"), 0),
])
def test_match_value(test_input, expected):
    assert match_value(*test_input) == expected

@pytest.mark.parametrize("test_input, expected", [
    ("A Y", 8),
    ("B X", 1),
    ("C Z", 6)
])
def test_score(test_input, expected):
    assert score(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
        (("Rock","DRAW"), "Rock"),
        (("Scissors","WIN"), "Rock"),
        (("Paper","LOSE"), "Rock"),
])
def test_find_strat_piece(test_input, expected):
    assert find_strat_piece(*test_input) == expected

@pytest.mark.parametrize("test_input, expected", [
    ("A Y", 4),
    ("B X", 1),
    ("C Z", 7)
])
def test_score_strat_action(test_input, expected):
    assert score_strat_action(test_input) == expected