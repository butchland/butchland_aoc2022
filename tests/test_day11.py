import pytest
from butchland_aoc2022.day11 import *


sm_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

@pytest.fixture()
def sm_samples():
    yield sm_input.splitlines()

def test_read_samples(sm_samples):
    assert len(sm_samples) == 27

def test_extract_lcm(sm_samples):
    lcm = extract_lcm(sm_samples)
    assert lcm == 96577

def test_generate_monkeys(sm_samples):
    monkeys = list(generate_monkeys(sm_samples))
    assert len(monkeys) == 4

    assert monkeys[0].id == 0
    assert monkeys[0].items == [79,98]
    assert monkeys[0].operation(1) == 19 
    assert monkeys[0].test == 23
    assert monkeys[0].action_false == 3
    assert monkeys[0].action_true == 2

    assert monkeys[1].id == 1
    assert monkeys[1].items == [54, 65, 75, 74]
    assert monkeys[1].operation(1) == 7 
    assert monkeys[1].test == 19
    assert monkeys[1].action_false == 0
    assert monkeys[1].action_true == 2

    assert monkeys[2].id == 2
    assert monkeys[2].items == [79, 60, 97]
    assert monkeys[2].operation(1) == 1 
    assert monkeys[2].test == 13
    assert monkeys[2].action_false == 3
    assert monkeys[2].action_true == 1

    assert monkeys[3].id == 3
    assert monkeys[3].items == [74]
    assert monkeys[3].operation(1) == 4 
    assert monkeys[3].test == 17
    assert monkeys[3].action_false == 1
    assert monkeys[3].action_true == 0

def test_generate_monkeys2(sm_samples):
    monkeys = list(generate_monkeys(sm_samples, divisor=3))
    assert len(monkeys) == 4

    assert monkeys[0].id == 0
    assert monkeys[0].items == [79,98]
    assert monkeys[0].operation(3) == 19 
    assert monkeys[0].test == 23
    assert monkeys[0].action_false == 3
    assert monkeys[0].action_true == 2

    assert monkeys[1].id == 1
    assert monkeys[1].items == [54, 65, 75, 74]
    assert monkeys[1].operation(15) == 7 
    assert monkeys[1].test == 19
    assert monkeys[1].action_false == 0
    assert monkeys[1].action_true == 2

    assert monkeys[2].id == 2
    assert monkeys[2].items == [79, 60, 97]
    assert monkeys[2].operation(3) == 3 
    assert monkeys[2].test == 13
    assert monkeys[2].action_false == 3
    assert monkeys[2].action_true == 1

    assert monkeys[3].id == 3
    assert monkeys[3].items == [74]
    assert monkeys[3].operation(9) == 4 
    assert monkeys[3].test == 17
    assert monkeys[3].action_false == 1
    assert monkeys[3].action_true == 0


def test_round_monkeys(sm_samples):
    monkeys = list(generate_monkeys(sm_samples, divisor=3))
    monkeys = round(monkeys)
    assert len(monkeys) == 4
    assert monkeys[0].id == 0
    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[0].operation(3) == 19 
    assert monkeys[0].test == 23
    assert monkeys[0].action_false == 3
    assert monkeys[0].action_true == 2

    assert monkeys[1].id == 1
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]

    assert monkeys[1].operation(15) == 7 
    assert monkeys[1].test == 19
    assert monkeys[1].action_false == 0
    assert monkeys[1].action_true == 2

    assert monkeys[2].id == 2
    assert monkeys[2].items == []

    assert monkeys[2].operation(3) == 3 
    assert monkeys[2].test == 13
    assert monkeys[2].action_false == 3
    assert monkeys[2].action_true == 1

    assert monkeys[3].id == 3
    assert monkeys[3].items == []
    assert monkeys[3].operation(9) == 4 
    assert monkeys[3].test == 17
    assert monkeys[3].action_false == 1
    assert monkeys[3].action_true == 0

def test_round_monkeys2(sm_samples):
    monkeys = list(generate_monkeys(sm_samples, divisor=3))
    
    monkeys = round(monkeys)
    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    monkeys = round(monkeys)
    assert monkeys[0].items == [695, 10, 71, 135, 350]
    assert monkeys[1].items == [43, 49, 58, 55, 362]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    monkeys = round(monkeys)
    assert monkeys[0].items == [16, 18, 21, 20, 122]
    assert monkeys[1].items == [1468, 22, 150, 286, 739]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

def test_run_rounds(sm_samples):
    monkeys = list(generate_monkeys(sm_samples, divisor=3))
    assert monkeys[0].inspections == 0
    assert monkeys[1].inspections == 0
    assert monkeys[2].inspections == 0
    assert monkeys[3].inspections == 0
    monkeys = run_rounds(monkeys)
    assert monkeys[0].inspections == 101
    assert monkeys[1].inspections == 95
    assert monkeys[2].inspections == 7
    assert monkeys[3].inspections == 105

def test_monkey_business(sm_samples):
    monkeys = list(generate_monkeys(sm_samples, divisor=3))
    monkeys = run_rounds(monkeys)
    mbusiness = monkey_business(monkeys)
    assert mbusiness == 10605

def test_long_no_reliefs(sm_samples):
    lcm = extract_lcm(sm_samples)
    monkeys = list(generate_monkeys(sm_samples, modulo=lcm, divisor=1))
    monkeys = run_rounds(monkeys, rounds=1)
    assert monkeys[0].inspections == 2
    assert monkeys[1].inspections == 4
    assert monkeys[2].inspections == 3
    assert monkeys[3].inspections == 6

    monkeys = run_rounds(monkeys, rounds=(20-1))
    assert monkeys[0].inspections == 99
    assert monkeys[1].inspections == 97
    assert monkeys[2].inspections == 8
    assert monkeys[3].inspections == 103

    monkeys = run_rounds(monkeys, rounds=(100 - 20))

    monkeys = run_rounds(monkeys, rounds=(500 - 100))
    monkeys = run_rounds(monkeys, rounds=(700 - 500))
    monkeys = run_rounds(monkeys, rounds=(800 - 700))

    monkeys = run_rounds(monkeys, rounds=(1_000 - 800))

    monkeys = run_rounds(monkeys, rounds=(10_000 - 1_000))
    assert monkeys[0].inspections == 52166
    assert monkeys[1].inspections == 47830
    assert monkeys[2].inspections == 1938
    assert monkeys[3].inspections == 52013
 
def test_long_no_reliefs2(sm_samples):
    lcm = extract_lcm(sm_samples)
    monkeys = list(generate_monkeys(sm_samples, modulo=lcm, divisor=1))
    monkeys = run_rounds(monkeys, rounds=1000)
    assert monkeys[0].inspections == 5204
    assert monkeys[1].inspections == 4792
    assert monkeys[2].inspections == 199
    assert monkeys[3].inspections == 5192


