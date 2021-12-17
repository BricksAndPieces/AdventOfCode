"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""

from aoc import *

inputs = puzzle_input(2, 2021, sample=False).split('\n')
inputs = [(line.split(" ")[0], int(line.split(" ")[1])) for line in inputs]

x1, y1 = 0, 0
x2, y2, a2 = 0, 0, 0
for (d, n) in inputs:
    if d == "forward":
        x1 += n
        x2 += n
        y2 += a2 * n
    if d == "down":
        y1 += n
        a2 += n
    if d == "up":
        y1 += -n
        a2 += -n

print(f'Part 1: {x1 * y1}')
print(f'Part 2: {x2 * y2}')
