__all__ = ["parse_line","generate_tokens", "process_commands"]

# day7 
import re
from fastcore.all import *

CD_CMD_PAT = r'\$ cd (.+)'
LS_CMD_PAT = r'\$ ls'
DIR_PAT = r'dir (.+)'
FSIZE_PAT = r'(\d+) (.+)'

def parse_line(line):
    m = re.match(CD_CMD_PAT, line)
    if m is not None:
        dir = m.groups()[0]
        return ("cd", dir.strip())
    m = re.match(LS_CMD_PAT, line)
    if m is not None:
        return ("ls",)
    m = re.match(DIR_PAT,line)
    if m is not None:
        dir = m.groups()[0]
        return ("dir", dir.strip())
    m = re.match(FSIZE_PAT, line)
    if m is not None:
        fsize = m.groups()[0]
        fname = m.groups()[1]
        return ("size", int(fsize), fname)
    return None

def generate_tokens(input):
    for line in input:
        token = parse_line(line)
        yield token


class Node:
    def __init__(self,name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children =  {}

    def add_child(self, child):
        self.children[child.name] = child

    def get_descendant(self):
        for child in self.children.values():
            yield child.get_descendant()
        yield self
class TokenProcessor:
    def __init__(self):
        self.nodes = []
        self.root = Node("/",None)
        self.current = self.root
        self.nodes.append(self.root)
    
    def process_token(self, token):
        if token[0] == "cd":
            if token[1] == "/":
                self.current = self.root
            elif token[1] == "..":
                previous = self.current
                current = self.current.parent
                if current == None:
                    raise ValueError("Could not go up higher, already at root")
                current.size += previous.size
                self.current = current
            else:
                if token[1] not in self.current.children:
                    raise ValueError(f'cd {token[1]} not a valid directory')
                current = self.current.children[token[1]]
                self.current = current
        elif token[0] == "size":
            self.current.size += token[1] # add size
        elif token[0] == "dir":
            child = Node(token[1],self.current)
            self.current.add_child(child)
            self.nodes.append(child)
    def return_current_to_root(self):
        while self.current != self.root:
            previous = self.current
            current = self.current.parent
            if current == None:
                raise ValueError("Could not go up higher, already at root")
            current.size += previous.size
            self.current = current

def process_commands(input):

    token_processor = TokenProcessor()

    for token in generate_tokens(input):
        token_processor.process_token(token)

    token_processor.return_current_to_root()

    return token_processor.nodes


        

