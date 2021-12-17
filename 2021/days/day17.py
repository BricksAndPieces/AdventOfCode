"""
--- Day 17: Trick Shot ---
https://adventofcode.com/2021/day/17
"""

from itertools import product
from aoc import *

inputs = puzzle_input(17, 2021, sample=False).split(', ')
target_x = [int(s) for s in (inputs[0].split('x=')[1]).split('..')]
target_y = [int(s) for s in (inputs[1][2:]).split('..')]

print(f'Part 1: {target_y[0] * (target_y[0] + 1) // 2}')

count = 0
for dx, dy in product(range(0, target_x[1] + 1), range(target_y[0], abs(target_y[0]))):
    x = y = 0
    while True:
        x += dx
        y += dy

        if (target_x[0] <= x <= target_x[1]) and (target_y[0] <= y <= target_y[1]):
            count += 1
            break
        elif (dx == 0 and not (target_x[0] <= x <= target_x[1])) or y < target_y[0]:
            break

        dx = max(0, dx - 1)
        dy -= 1

print(f'Part 2: {count}')
