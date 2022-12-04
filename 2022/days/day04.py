"""
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4
"""

from aoc import *

inputs = puzzle_input(4, 2022, sample=False).split('\n')
pairs = [[[int(c) for c in b.split('-')] for b in a.split(',')] for a in inputs]

def full_overlap(a, b):
    return (a[0] <= b[0] and b[1] <= a[1]) or (b[0] <= a[0] and a[1] <= b[1])

num_overlap = sum(full_overlap(*a) for a in pairs)
print(f'Part 1: {num_overlap}')

def any_overlap(a, b):
    return b[0] <= a[0] <= b[1] or a[0] <= b[0] <= a[1]

num_overlap = sum(any_overlap(*a) for a in pairs)
print(f'Part 2: {num_overlap}')
