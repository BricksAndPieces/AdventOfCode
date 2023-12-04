"""
--- Day 4: Scratchcards ---
https://adventofcode.com/2023/day/4
"""

from functools import lru_cache
from aoc import *
import re

inputs = puzzle_input(4, 2023, sample=False).split('\n')

@lru_cache(maxsize=None)
def solve(line, part) -> int:
    id = int(re.search(r'\d+', line).group())
    line = line.split(': ')[1]
    expect, actual = line.split(' | ')
    expect = [int(x) for x in expect.split(' ') if x != '']
    actual = [int(x) for x in actual.split(' ') if x != '']

    ret = 1
    val = 0
    for v in actual:
        if v in expect:
           ret += solve(inputs[id + val], part)
           val += 1

    return ret if part == 2 else 2 ** (val-1) if val else 0

print(f'Part 1: {sum(solve(line, 1) for line in inputs)}')
print(f'Part 2: {sum(solve(line, 2) for line in inputs)}')
