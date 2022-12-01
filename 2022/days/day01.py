"""
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1
"""

from aoc import *

inputs = puzzle_input(1, 2022, sample=False).split('\n\n')
calories = sorted([sum(ints(a)) for a in inputs])

print(f'Part 1: {calories[-1]}')
print(f'Part 2: {sum(calories[-3:])}')
