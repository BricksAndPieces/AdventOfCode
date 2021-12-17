"""
--- Day 5: Hydrothermal Venture ---
https://adventofcode.com/2021/day/5
"""

from collections import defaultdict
from aoc import *

inputs = puzzle_input(5, 2021, sample=True).split('\n')
inputs = [[(int((x := c.split(','))[0]), int(x[1])) for c in line.split(' -> ')] for line in inputs]


def solve(part1):
    vents = defaultdict(lambda: 0)
    for [(x1, y1), (x2, y2)] in inputs:
        xs = [*(range(x1, x2 + 1) if x1 < x2 else reversed(range(x2, x1 + 1)))]
        ys = [*(range(y1, y2 + 1) if y1 < y2 else reversed(range(y2, y1 + 1)))]

        if len(xs) == 1:
            xs *= len(ys)
        elif len(ys) == 1:
            ys *= len(xs)
        elif part1:
            continue

        for c in zip(xs, ys):
            vents[c] += 1

    return sum(vents[e] >= 2 for e in vents)


print(f'Part 1: {solve(True)}')
print(f'Part 2: {solve(False)}')
