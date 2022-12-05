"""
--- Day 5: Supply Stacks ---
https://adventofcode.com/2022/day/5
"""

from copy import deepcopy
from aoc import *

inputs = puzzle_input(5, 2022, sample=False)

stacks_raw = inputs.split('\n\n')[0].split('\n')
stacks = [[] for _ in range((len(stacks_raw[0])+1)//4)]

for line in reversed(stacks_raw[:-1]):
    letters = line[1::4]
    for i, letter in enumerate(letters):
        if letter != ' ':
            stacks[i].append(letter)

instructs_raw = inputs.split('\n\n')[1].split('\n')
instructs = [[int(i) for i in a.split() if i.isdigit()] for a in instructs_raw]

stacks_initial = deepcopy(stacks)
for instruct in instructs:
    for _ in range(instruct[0]):
        stacks[instruct[2]-1].append(stacks[instruct[1]-1].pop())

top_crates = ''.join(a[-1] for a in stacks)
print(f'Part 1: {top_crates}')

stacks = stacks_initial
for instruct in instructs:
    stacks[instruct[2]-1] += stacks[instruct[1]-1][-instruct[0]:]
    del stacks[instruct[1]-1][-instruct[0]:]

top_crates = ''.join(a[-1] for a in stacks)
print(f'Part 2: {top_crates}')
