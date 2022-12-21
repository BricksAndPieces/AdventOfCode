"""
--- Day 20: Grove Positioning System ---
https://adventofcode.com/2022/day/20
"""

from aoc import *

def solve(rep, multiplier):
    vals = [(n, v*multiplier) for n, v in enumerate(ints(puzzle_input(20, 2022, sample=False), '\n'))]
    vals_copy = vals.copy()

    for _ in range(rep):
        for n, v in vals_copy:
            i = vals.index((n, v))
            vals.pop(i)
            vals.insert((i+v) % len(vals), (n, v))

    zero = next(i for i, (_, v) in enumerate(vals) if v == 0)
    return sum(vals[(zero + i) % len(vals)][1] for i in [1000, 2000, 3000])


print(f'Part 1: {solve(1, 1)}')
print(f'Part 2: {solve(10, 811589153)}')

