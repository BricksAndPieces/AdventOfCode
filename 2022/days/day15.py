"""
--- Day 15: Beacon Exclusion Zone ---
https://adventofcode.com/2022/day/15
"""

import re
import math
from aoc import *

sample = False
inputs = puzzle_input(15, 2022, sample=sample).split('\n')
pairs = [[int(s) for s in re.findall('-?\d+\d*', a)] for a in inputs]
row = 10 if sample else 2_000_000

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

exclude = [math.inf, -math.inf]
for sx, sy, bx, by in pairs:
    d = dist(sx, sy, bx, by)
    r = (d-abs(sy-row))
    exclude[0] = min(exclude[0], sx-r)
    exclude[1] = max(exclude[1], sx+r)

print(f'Part 1: {exclude[1] - exclude[0]}')

def in_sensor_range(x, y):
    for sx, sy, bx, by in pairs:
        d1 = dist(sx, sy, bx, by)
        d2 = dist(sx, sy, x, y)
        if d2 <= d1:
            return True
    
    return False

max_bounds = 20 if sample else 4_000_000
neg_combos = [[1, 1], [-1, 1], [1, -1], [-1, -1]]

tuning_freq = None
for sx, sy, bx, by in pairs:
    d = dist(sx, sy, bx, by)+1
    for dx in range(0, d+1):
        dy = d - dx
        x, y = sx+dx, sy+dy

        if (0 <= x <= max_bounds and 0 <= y <= max_bounds):
            if not any(in_sensor_range(nx*x, ny*y) for nx, ny in neg_combos):
                tuning_freq = x * 4_000_000 + y

    if tuning_freq is not None:
        break

print(f'Part 2: {tuning_freq}')
