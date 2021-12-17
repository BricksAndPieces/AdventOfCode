"""
--- Day 7: The Treachery of Whales ---
https://adventofcode.com/2021/day/7
"""

from aoc import *


def solve(crabs, f):
    return min(sum(f(abs(x - n)) for x in crabs) for n in range(max(crabs) + 1))


inputs = ints(puzzle_input(7, 2021, sample=False), ',')
print(f'Part 1: {solve(inputs, lambda x: x)}')
print(f'Part 2: {solve(inputs, lambda x: x * (x + 1) // 2)}')
