"""
Problem here
"""

from aoc import *

inputs = [int(s) for s in puzzle_input(1, 2017, sample=False)]
solve = lambda jump: sum(n for i, n in enumerate(inputs) if n == inputs[(i + jump) % len(inputs)])

print(f'Part 1: {solve(1)}')
print(f'Part 2: {solve(len(inputs) // 2)}')
