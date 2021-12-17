"""
--- Day 11: Dumbo Octopus ---
https://adventofcode.com/2021/day/11
"""

from itertools import product
from aoc import *

inputs = puzzle_input(11, 2021, sample=False).split('\n')
inputs = [[int(x) for x in s] for s in inputs]


def increment_neighbors(x, y, matrix):
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        valid = 0 <= x+dx < len(matrix) and 0 <= y+dy < len(matrix[0])
        if (dx, dy) != (0, 0) and valid:
            matrix[x + dx][y + dy] += 1


def step(matrix):
    flashes = 0
    matrix = [[x + 1 for x in line] for line in matrix]

    while any(x > 9 for line in matrix for x in line):
        for x, y in product(range(len(matrix[0])), range(len(matrix))):
            if matrix[x][y] > 9:
                flashes += 1
                matrix[x][y] = -9999999  # Big negative number

                increment_neighbors(x, y, matrix)

    matrix = [[max(x, 0) for x in line] for line in matrix]
    return matrix, flashes


step_count = flash_count = 0
while True:
    inputs, flash = step(inputs)
    flash_count += flash if step_count < 100 else 0
    step_count += 1

    if all(x == 0 for line in inputs for x in line):
        break

print(f'Part 1: {flash_count}')
print(f'Part 2: {step_count}')
