__all__ = ["process_moves","execute_move", "move_rope", "init_rope","Pos"]

# day9 
import math

from collections import namedtuple

Pos = namedtuple("Pos","r c") # position : row, column

def init_rope(knots=2, init_pos=Pos(11,15)):
    return tuple([init_pos] * knots)

def move_head(h, dir):
    if dir == "U":
        return Pos(h.r-1, h.c)
    elif dir == "D":
        return Pos(h.r+1, h.c)
    elif dir == "L":
        return Pos(h.r, h.c-1)
    else: # dir = "R"
        return Pos(h.r, h.c+1)

def is_adjacent(p1,p2):
    return abs(p1.c - p2.c) < 2 and abs(p1.r - p2.r) < 2

def is_diagonal(p1,p2):
    return (p1.r != p2.r) and (p1.c != p2.c)

def distance(p1,p2):
    return Pos(p1.r-p2.r, p1.c-p2.c)

def abs_distance(p1,p2):
    dist = distance(p1,p2)
    return Pos(abs(dist.r), abs(dist.c))

def same_row(p1,p2):
    return p1.r == p2.r

def move_rope(rope,dir):
    new_h = move_head(rope[0],dir)
    new_rope = [new_h]
    for i,k in enumerate(rope[1:]):
        dist = distance(new_h, k)
        if is_adjacent(new_h,k):
            new_k = k # no movement
        elif not is_diagonal(new_h, k):
            if same_row(new_h, k):
                new_k = Pos(k.r, k.c + int(math.copysign(1, dist.c)))
            else: # same column
                new_k = Pos(k.r + int(math.copysign(1,dist.r)), k.c)   
        else: # is_diagonal(new_h, k):
            new_k = Pos(k.r+int(math.copysign(1, dist.r)),
                        k.c+int(math.copysign(1, dist.c)))
        new_rope.append(new_k)
        new_h = new_k
    return tuple(new_rope)

def parse_move(move):
    dir,cnt = move.split(" ")
    return (dir, int(cnt))

def execute_move(rope, move):
    dir, cnt = parse_move(move)
    occupieds = set([rope[-1]])
    for i in range(cnt):
        rope = move_rope(rope, dir)
        occupieds.add(rope[-1])
    return rope, occupieds

def process_moves(moves, rope=None, knots=2,init_pos=Pos(11,15)):
    if rope is None:
        rope = init_rope(knots=knots, init_pos=init_pos)
    all_occupieds = set([rope[-1]])
    for move in moves:
        rope, occupieds = execute_move(rope, move)
        all_occupieds.update(occupieds)
    return rope,all_occupieds
