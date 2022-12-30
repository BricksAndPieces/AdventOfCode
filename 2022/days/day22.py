"""
--- Day 22: Monkey Map ---
https://adventofcode.com/2022/day/22
"""

from collections import defaultdict, deque
from itertools import combinations, permutations, product
from functools import lru_cache, reduce
import numpy as np
import re

from aoc import *

# formatting puzzle input
grid, moves = puzzle_input(22, 2022, sample=True).split('\n\n')
grid = grid.split('\n')
max_width = max(len(s) for s in grid)
for i, s in enumerate(grid):
    grid[i] += ' ' * (max_width - len(s))

moves = [*moves]
for i in reversed(range(1, len(moves))):
    if moves[i].isdigit() and moves[i-1].isdigit():
        moves[i-1] += moves[i]
        del moves[i]
moves = [int(m) if m.isdigit() else m for m in moves]

# following path
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = next(i for i, v in enumerate(grid[0]) if v == '.'), 0
dir = 0

def in_bounds(x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

for move in moves:
    print(x, y)
    if move == 'L':
        dir = (dir-1) % 4
    elif move == 'R':
        dir = (dir+1) % 4
    else:
        for _ in range(move):
            nx, ny = x + DIRS[dir][0], y + DIRS[dir][1]
            if not in_bounds(nx, ny) or grid[ny][nx] == ' ':
                while in_bounds(nx, ny) and grid[ny][nx] != ' ':
                    nx, ny = nx - DIRS[dir][0], ny - DIRS[dir][1]
                nx, ny = nx + DIRS[dir][0], ny + DIRS[dir][1]

            print(nx, ny)
            if grid[ny][nx] == '#':
                break
            else:
                x, y = nx, ny

print(x, y)


print(f'Part 1: {0}')
print(f'Part 2: {0}')
