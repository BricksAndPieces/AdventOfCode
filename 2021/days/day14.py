"""
--- Day 14: Extended Polymerization ---
https://adventofcode.com/2021/day/14
"""

from collections import Counter
from aoc import *

inputs = puzzle_input(14, 2021, sample=False).split('\n\n')
templates = {(x := a.split(' -> '))[0]: x[1] for a in inputs[1].split('\n')}
polymer = inputs[0]


def solve(n):
    counter = Counter(polymer[i:i + 2] for i in range(len(polymer) - 1))
    for _ in range(n):
        new_counter = Counter()
        for k, v in counter.items():
            new_counter[k] -= v
            new_counter[k[0] + templates[k]] += v
            new_counter[templates[k] + k[1]] += v

        counter += new_counter

    letter_counter = Counter()
    for k, v in counter.items():
        letter_counter[k[0]] += v
        letter_counter[k[1]] += v

    # Start and end letters (not paired)
    letter_counter[polymer[0]] += 1
    letter_counter[polymer[-1]] += 1

    # Each letter was counted twice so // 2
    counts = [v for k, v in letter_counter.items()]
    return (max(counts) - min(counts)) // 2


print(f'Part 1: {solve(10)}')
print(f'Part 2: {solve(40)}')
