__all__ = ["generate_monkeys", "round","run_rounds", "monkey_business","relief","no_relief"]

# day11 
import re
from typing import Optional, Callable
from numba import jit
class Monkey:
    def __init__(self):
        self.inspections = 0
        self.id:Optional[int] = None
        self.items:list[int] = []
        self.operation:Optional[Callable] = None
        self.test:Optional[int] = None
        self.action_true:Optional[int] = None
        self.action_false:Optional[int] = None

monkey_pat = r'Monkey (\d+):'
item_pat = r"Starting items: (.+)"
op_pat = r"Operation: new = (.+)"
test_pat = r"Test: divisible by (\d+)"
action_true_pat = r"If true: throw to monkey (\d+)"
action_false_pat = r"If false: throw to monkey (\d+)"


def generate_monkeys(inputs):
    monkey = Monkey()
    for line in inputs:
        if len(line) == 0:
            # handle line break between monkeys
            yield monkey
            monkey = Monkey()
            continue

        monkey_match = re.search(monkey_pat, line)
        if monkey_match is not None:
            monkey.id = int(monkey_match.groups()[0])
            continue

        item_match = re.search(item_pat, line)
        if item_match is not None:
            item_str = item_match.groups()[0]
            items = [int(item.strip()) for item in item_str.split(",")]
            monkey.items = items
            continue

        op_match = re.search(op_pat,line)
        if op_match is not None:
            lambda_body = op_match.groups()[0]
            lambda_str = f'lambda old: {lambda_body}'
            lambda_func = eval(lambda_str)
            monkey.operation = lambda_func
            continue

        test_match = re.search(test_pat,line)
        if test_match is not None:
            test = test_match.groups()[0]
            monkey.test = int(test)
            continue

        action_true_match = re.search(action_true_pat,line)
        if action_true_match is not None:
            action_true = action_true_match.groups()[0]
            monkey.action_true = int(action_true)
            continue

        action_false_match = re.search(action_false_pat,line)
        if action_false_match is not None:
            action_false = action_false_match.groups()[0]
            monkey.action_false = int(action_false)

    yield monkey        
        

def relief(worry:int) -> int:
    return worry // 3 

def no_relief(worry:int) -> int:
    return worry 

@jit(no_python=True)
def round(monkeys:list[Monkey], relief=relief) -> list[Monkey]:
    for monkey in monkeys:
        mitems = monkey.items.copy()
        monkey.inspections += len(mitems)
        for item in mitems:
            # inspect
            new_worry = monkey.operation(item)
            # relief
            new_worry = relief(new_worry)
            # test
            if monkey.test is not None:
                # throw
                remainder = new_worry % monkey.test
                if remainder == 0:
                    monkeys[monkey.action_true].items.append(new_worry)
                else:
                    monkeys[monkey.action_false].items.append(new_worry) # type: ignore
            del monkey.items[0] # delete after throwing
    return monkeys

@jit(nopython=True)
def run_rounds(monkeys:list[Monkey], rounds:int=20, relief=relief)-> list[Monkey]:
    for _ in range(rounds):
        monkeys = round(monkeys, relief=relief)
    return monkeys


def monkey_business(monkeys:list[Monkey]) -> int:
    inspections = [m.inspections for m in monkeys]
    if len(inspections) < 2:
        return 0
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


