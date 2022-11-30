"""
--- Day 25: Sea Cucumber ---
https://adventofcode.com/2021/day/25
"""

from copy import deepcopy
from itertools import product
from aoc import *


def step(state):
    new_state = deepcopy(state)
    for x, y in product(range(len(state)), range(len(state[0]))):
        if state[x][y] == '>' and state[x][(y+1) % len(state[0])] == '.':
            new_state[x][(y+1) % len(state[0])] = '>'
            new_state[x][y] = '.'

    state = deepcopy(new_state)
    for x, y in product(range(len(state)), range(len(state[0]))):
        if state[x][y] == 'v' and state[(x+1) % len(state)][y] == '.':
            new_state[(x + 1) % len(state)][y] = 'v'
            new_state[x][y] = '.'

    return new_state


state = [list(line) for line in puzzle_input(25, 2021, sample=False).split('\n')]
count = 1

while True:
    new_state = step(state)
    if state == new_state:
        break

    state = new_state
    count += 1

print(f'Part 1: {count}')
print(f'Part 2: {0}')
