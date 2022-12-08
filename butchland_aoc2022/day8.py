# __all__ = []

import fastcore.all as fc

# day8
def init_grid(input):
    grid = []
    for row in input:
        grid.append([int(c)for c in row])
    return grid

def shape(grid):
    # rows,cols
    return (len(grid),len(grid[0]))

def elt(grid,r,c):
    return grid[r][c]

def left(grid,r,c):
    return grid[r][:c]

def right(grid,r,c):
    return grid[r][c+1:]

def above(grid,r,c):
    result = []
    for i in range(r):
        result.append(grid[i][c])
    return result

def below(grid, r, c):
    result = []
    for i in range(r+1,len(grid)):
        result.append(grid[i][c])
    return result

directions = [left,right,above,below]

def is_visible(grid,r,c): 
    e = elt(grid,r,c) 
    for d in directions:
        blockers = d(grid,r,c)
        if max(blockers) < e:
            return True
    return False

def count_visible(grid):
    r,c = shape(grid)
    count = (r+c)*2 - 4
    for i in range(1,r-1):
        for j in range(1,c-1):
            if is_visible(grid,i,j):
                count += 1
    return count

def count_seen(v,e):
    i = -1
    for i,p in enumerate(v):
        if p >= e: 
            return i + 1
    return i + 1

def scenic_score(grid, r,c):
    nr,nc = shape(grid)
    e = elt(grid,r,c)
    seen = 1
    vl = fc.L(left(grid,r,c))
    vl.reverse()
    seen *= count_seen(vl,e)
    vr = right(grid,r,c)
    seen *= count_seen(vr,e)
    va = fc.L(above(grid,r,c))
    va.reverse()
    seen *= count_seen(va,e)
    vb = below(grid,r,c)
    seen *= count_seen(vb,e)
    return seen

def highest_scenic_score(grid):
    nr,nc = shape(grid)
    scenic_scores = []
    for i in range(1,nr-1):
        for j in range(1,nc-1):
            scenic_scores.append(scenic_score(grid,i,j)) 
    return max(scenic_scores)
    
    


