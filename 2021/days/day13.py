"""
--- Day 13: Transparent Origami ---
https://adventofcode.com/2021/day/13
"""

from itertools import product
from aoc import *

inputs = puzzle_input(13, 2021, sample=False).split('\n\n')
sheet_coords = [ints(a, ',') for a in inputs[0].split('\n')]
fold_instructions = [((line := instr[11:].split('='))[0], int(line[1])) for instr in inputs[1].split('\n')]

for n, instr in enumerate(fold_instructions):
    max_x, max_y = max(sheet_coords)

    new_coords = set()
    for (x, y) in sheet_coords:
        if instr[0] == 'x':
            new_coords.add((x, y) if x < instr[1] else (max_x - x, y))
        if instr[0] == 'y':
            new_coords.add((x, y) if y < instr[1] else (x, max_y - y))

    sheet_coords = list(new_coords)

    if n == 0:
        print(f'Part 1: {len(sheet_coords)}')

max_x = max(a for a, _ in sheet_coords) + 1
max_y = max(a for _, a in sheet_coords) + 1
draw = [['   '] * max_x for _ in range(max_y)]

for x, y in product(range(max_x), range(max_y)):
    if (x, y) in sheet_coords:
        draw[y][x] = ' O '

print(f'Part 2:')
for line in draw:
    print(''.join(line))
