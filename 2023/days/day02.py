"""
--- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2
"""

from collections import defaultdict
from aoc import *

inputs = puzzle_input(2, 2023, sample=False).split('\n')

def solve(line, p):
    splits = line.split()
    id = int(splits[1][:-1])
    line = ' '.join(splits[2:])
    turns = line.split('; ')

    stuff = defaultdict(lambda: 0)
    for turn in turns:
        parts = turn.split(', ')

        for part in parts:
            n, color = part.split()
            stuff[color] = max(int(n), stuff[color])
        
        if p == 1 and (stuff['red'] > 12 or stuff['green'] > 13 or stuff['blue'] > 14):
            return 0
    
    return id if p == 1 else stuff['red'] * stuff['green'] * stuff['blue']


print(f'Part 1: {sum(solve(line, 1) for line in inputs)}')
print(f'Part 2: {sum(solve(line, 2) for line in inputs)}')
