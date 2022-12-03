"""
--- Day 3: Rucksack Reorganization ---
https://adventofcode.com/2022/day/3
"""

from aoc import *

inputs = puzzle_input(3, 2022, sample=False).split('\n')

def calc_scores(g):
    common = (set(a[0]).intersection(*a[1:]).pop() for a in g)
    return sum(ord(a)-96 if a.islower() else ord(a)-38 for a in common)

group = ((a[:len(a)//2], a[len(a)//2:]) for a in inputs)
print(f'Part 1: {calc_scores(group)}')

group=zip(inputs[::3], inputs[1::3], inputs[2:][::3])
print(f'Part 2: {calc_scores(group)}')
