"""
--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6
"""

from functools import lru_cache
from aoc import *


@lru_cache
def fish(timer, days):
    if days == 0:
        return 1
    elif timer == 0:
        return fish(6, days - 1) + fish(8, days - 1)
    else:
        return fish(timer - 1, days - 1)


inputs = ints(puzzle_input(6, 2021, sample=False), ',')
print(f'Part 1: {sum(fish(a, 80) for a in inputs)}')
print(f'Part 2: {sum(fish(a, 256) for a in inputs)}')
