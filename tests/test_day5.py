import pytest
from butchland_aoc2022.day5 import *

input =  """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

@pytest.fixture()
def samples():
    yield input.splitlines()

def test_get_stack_count(samples):
    assert get_stack_count(samples) == 3

def test_init_stacks():
    assert init_stacks(3) == [[],[],[]]

def test_split_stack_moves(samples):
    stacks,moves = split_stack_moves(samples)
    assert len(stacks) == 3
    assert len(moves) == 4

def test_build_stacks(samples):
    n_stacks = get_stack_count(samples)
    stacks,_ = split_stack_moves(samples)
    real_stacks = build_stacks(stacks,n_stacks)
    assert len(real_stacks) == 3
    assert tuple([len(s) for s  in real_stacks]) == (2,3,1)

def test_parse_move():
    assert parse_move("move 1 from 2 to 1") == (1,2,1)

def test_execute_move():
    stacks = [["Z","N"],["M","C","D"],["P"]]
    stacks = execute_move(stacks,1,2,1)
    assert tuple([len(s) for s  in stacks]) == (3,2,1)
    assert stacks[0][-1] == "D"     