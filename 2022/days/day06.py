"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6
"""

from aoc import *

inputs = puzzle_input(6, 2022, sample=False)

def first_unique(l):
    return next(n+l for n, _ in enumerate(inputs) if len(set(inputs[n:n+l])) == l)

print(f'Part 1: {first_unique(4)}')
print(f'Part 2: {first_unique(14)}')
