"""
--- Day 12: Passage Pathing ---
https://adventofcode.com/2021/day/12
"""

from collections import defaultdict
from aoc import *

inputs = puzzle_input(12, 2021, sample=False).split('\n')
cave_paths = defaultdict(lambda: [])
for line in inputs:
    a, b = line.split('-')
    cave_paths[a].append(b)
    cave_paths[b].append(a)


def find_path(current, past_caves, went_twice):
    num = 0
    for option in cave_paths[current]:
        if option == 'end':
            num += 1
            continue
        elif option == 'start':
            continue
        elif option.islower() and option in past_caves and not went_twice:
            num += find_path(option, past_caves + [current], True)

        if not (option.islower() and option in past_caves):
            num += find_path(option, past_caves + [current], went_twice)

    return num


print(f'Part 1: {find_path("start", [], True)}')
print(f'Part 2: {find_path("start", [], False)}')
