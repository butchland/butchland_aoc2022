__all__ = ["parse_line"]

# day7 
import re

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
