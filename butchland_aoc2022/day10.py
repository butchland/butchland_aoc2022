__all__ = ["Cmd","CPU", "sum_strengths"]

import fastcore.all as fc
from collections import namedtuple

Cmd = namedtuple("Cmd", "cmd value")
# day10 

def parse_input(input):
    if input == "noop":
        return Cmd("noop",None)
    cmd, value = input.split(" ")
    return Cmd(cmd,int(value))

class CPU:
    def __init__(self, cmds):
        self.cmds = cmds
        self.reset()
        # self.pc = 0
        # self.X = 1
        # self.cycle = 0
        # self.pending = False
        # self.R = None

    def reset(self):
        self.pc = 0
        self.X = 1
        self.cycle = 0
        self.pending = False
        self.R = None
    

    def cycles(self):
        self.reset()
        while self.pc < len(self.cmds):
            self.cycle += 1
            cmd,v = parse_input(self.cmds[self.pc])
            if cmd == "noop":
                self.pc += 1
                yield (self.cycle, self.X)
            else:
                x = self.X
                if self.R is not None:
                    self.X += self.R
                    self.R = None
                    self.pc += 1
                else:
                    self.R = v
                yield (self.cycle, x)

    def signal_strengths(self):
        for cycle,X in self.cycles():
            if (cycle - 20) % 40 == 0:
                yield cycle * X
       
    def draw_pixel(self):       
        for cycle,X in self.cycles():
            position = (cycle - 1) % 40
            if position in set([X-1,X,X+1]):
                yield "#"
            else:
                yield "."


    def debug_draw_pixel(self):
      
        for cycle, X in self.cycles():
            position = (cycle - 1) % 40
            if position in set([X-1,X,X+1]):
                pixel = "#"
            else:
                pixel = "."
            yield (cycle,X, pixel, position)
            
    
def sum_strengths(cmds, seq_len=6):
    cpu = CPU(cmds)
    strengths = list(cpu.signal_strengths())
    return sum(strengths[:seq_len])