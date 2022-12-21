__all__ = [ "extract_lcm",
            "generate_monkeys", 
            "round",
            "run_rounds", 
            "monkey_business",
          ]

# day11 
import re
from typing import Optional, Callable
import math

class Monkey:
    def __init__(self):
        self.inspections = 0
        self.id:Optional[int] = None
        self.items:list[int] = []
        self.operation:Optional[Callable[[int],int]] = None
        self.test:Optional[int] = None
        self.action_true:Optional[int] = None
        self.action_false:Optional[int] = None

monkey_pat = r'Monkey (\d+):'
item_pat = r"Starting items: (.+)"
op_pat = r"Operation: new = (.+)"
test_pat = r"Test: divisible by (\d+)"
action_true_pat = r"If true: throw to monkey (\d+)"
action_false_pat = r"If false: throw to monkey (\d+)"

def extract_lcm(inputs):
    divs = []
    for line in inputs:
        test_match = re.search(test_pat,line)
        if test_match is not None:
            test = test_match.groups()[0]
            divs.append(int(test))
    return math.lcm(*divs)
        
def generate_monkeys(inputs, modulo=None, divisor=1):
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
            if modulo is not None:
                lambda_str = f"lambda old: (({lambda_body}) // {divisor}) % {modulo}"
            else:
                lambda_str = f"lambda old: (({lambda_body}) // {divisor})"
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
        


def compute_new_worries(mitems:list[int], operation:Callable[[int],int]):
    return [operation(item) for item in mitems]

def round(monkeys:list[Monkey]) -> list[Monkey]:    
    for monkey in monkeys:
        if len(monkey.items) > 0:
            mitems = monkey.items.copy()
            monkey.inspections += len(mitems)
            new_worries = compute_new_worries(mitems, monkey.operation) # type: ignore        
            action_true = [new_worry for new_worry in new_worries if (new_worry % monkey.test) == 0] # type: ignore     
            action_false =  [new_worry for new_worry in new_worries if (new_worry % monkey.test) != 0] # type: ignore     
            monkeys[monkey.action_true].items.extend(action_true)  # type: ignore 
            monkeys[monkey.action_false].items.extend(action_false) # type: ignore
            del monkey.items
            monkey.items = [] # delete after throwing
    return monkeys

# # @jit()
def run_rounds(monkeys:list[Monkey], rounds:int=20)-> list[Monkey]:
    for _ in range(rounds):
        monkeys = round(monkeys)
    return monkeys


def monkey_business(monkeys:list[Monkey]) -> int:
    inspections = [m.inspections for m in monkeys]
    if len(inspections) < 2:
        return 0
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


