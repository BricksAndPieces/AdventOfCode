"""
--- Day 8: Treetop Tree House ---
https://adventofcode.com/2022/day/8
"""

from functools import partial
from aoc import *

inputs = puzzle_input(8, 2022, sample=False).split('\n')
grid = [[int(c) for c in s] for s in inputs]
grid_t = list(map(list, zip(*grid)))

visible = 2 * (len(grid) + len(grid[0])) - 4
max_score = 0

def dir_score(val, dir):
    return next((i+1 for i, v in enumerate(dir) if v >= val), len(dir))

for x in range(1, len(grid)-1):
    for y in range(1, len(grid[0])-1):
        dirs = [
            grid[x][y+1:],
            grid[x][:y][::-1],
            grid_t[y][x+1:],
            grid_t[y][:x][::-1]
        ]

        sightlines = map(max, dirs)
        if grid[x][y] > min(sightlines):
            visible += 1

        score = mult(map(partial(dir_score, grid[x][y]), dirs))
        max_score = max(max_score, score)

print(f'Part 1: {visible}')
print(f'Part 2: {max_score}')
