__all__ = ["get_stack_count","init_stacks", "split_stack_moves", "build_stacks", "parse_move", "execute_move","execute_move2", "process_moves","process_moves2","get_top_elements"]

from fastcore.all import *
# day5 

def get_stack_count(
        input: list[str], # list of strings
    ) -> int:
    """Return the count of stacks given the input"""
    return(len(input[0]) + 1)//4

def init_stacks(
        n: int, # n of stacks
    ) -> list[list[str]]:
    """Create a list of `n` stacks"""
    return [[] for i in range(n)]


def split_stack_moves(
        samples:list[str], # list of strings
    ) -> any:  # type: ignore
    """Split the input and separate the stack section from the moves"""
    lsamples = L(samples)
    mark = lsamples.argfirst(lambda s: len(s) == 0)
    return (samples[:mark][:-1], samples[mark:][1:])

def build_stacks(
        stack_inputs:list[str], # list of strings representing a list of stacks
        n_stacks:int, # number of stacks
    ) -> list[list[str]]:
    """Build the real stack structure from the printed version"""
    stacks = init_stacks(n_stacks)
    levels = len(stack_inputs)
    for i in range(levels-1,-1,-1):
        s = stack_inputs[i]
        for j in range(n_stacks):
            pos = j*4+1
            if s[pos] != " ":
                stacks[j].append(s[pos])
    return stacks

def parse_move(
        move:str, # string with format `move n from a to b`
    ) -> (int,int,int):  # type: ignore
    """Parse the move statement and return the ntokens,from,to values"""
    pat = r'move (\d+) from (\d+) to (\d+)'
    m = re.match(pat, move)
    if m is None:
        raise ValueError(f"Invalid move for {move}")
    return tuple([int(d) for d in m.groups()])

def execute_move(
        stacks:list[list[str]], # list of stacks of tokens 
        n_tokens:int, # count of tokens to move 
        from_stack:int, # from the stack (start from position 1) 
        to_stack:int, # to the stack (start from position 1)
    ):
    """Executes a move of n_tokens from a stack to another stack"""
    for i in range(n_tokens):
        t = stacks[from_stack-1].pop()
        stacks[to_stack-1].append(t)
    return stacks

def execute_move2(
        stacks:list[list[str]], # list of stacks of tokens 
        n_tokens:int, # count of tokens to move 
        from_stack:int, # from the stack (start from position 1) 
        to_stack:int, # to the stack (start from position 1)
    ):
    """Executes a move of n_tokens from a stack to another stack"""
    stack_holder = []
    for i in range(n_tokens):
        t = stacks[from_stack-1].pop()
        stack_holder.append(t)

    for i in range(n_tokens):
        t = stack_holder.pop()
        stacks[to_stack-1].append(t)
    return stacks


def process_moves(
        input: list[str], # inputs with stacks and moves
    ):
    """Initializes the stacks and processes the moves"""
    n_stacks = get_stack_count(input)
    stacks,moves = split_stack_moves(input)
    stacks = build_stacks(stacks,n_stacks)
    for m in moves:
        pm = parse_move(m)
        if pm is not None:
            execute_move(stacks, *pm)
    return stacks

def process_moves2(
        input: list[str], # inputs with stacks and moves
    ):
    """Initializes the stacks and processes the moves for part 2"""
    n_stacks = get_stack_count(input)
    stacks,moves = split_stack_moves(input)
    stacks = build_stacks(stacks,n_stacks)
    for m in moves:
        pm = parse_move(m)
        if pm is not None:
            execute_move2(stacks, *pm)
    return stacks

def get_top_elements(
        stacks:list[list[str]], # a list of stacks of token
    ):
    """Gets the top tokens from each stack and concatenates to form a string"""
    result = []
    for stack in stacks:
        t = stack.pop()
        stack.append(t)
        result.append(t)
    return "".join(result)
    
    
