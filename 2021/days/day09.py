"""
--- Day 9: Smoke Basin ---
https://adventofcode.com/2021/day/9
"""

from aoc import *

inputs = puzzle_input(9, 2021, sample=False).split('\n')
inputs = [[int(x) for x in i] for i in inputs]


def valid_point(x, y):
    return 0 <= x <= len(inputs) - 1 and 0 <= y <= len(inputs[0]) - 1


def is_lowest(x, y):
    return inputs[x][y] < min(
        inputs[x + dx][y + dy] for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if valid_point(x + dx, y + dy)
    )


lowest = [[(x, y) for y in range(len(inputs[0])) if is_lowest(x, y)] for x in range(len(inputs))]
lowest = reduce(lambda a, b: a + b, lowest, [])  # Flattened 2d array into 1d array
print(f'Part 1: {sum(inputs[x][y] + 1 for (x, y) in lowest)}')


def flood_fill(x, y):
    amt = 1
    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        pt = (x + dx, y + dy)
        if valid_point(*pt) and 9 != inputs[x + dx][y + dy] > inputs[x][y]:
            amt += flood_fill(*pt)
            inputs[x+dx][y+dy] = 9  # set seen locations to 9 to prevent overlap

    return amt


flooded = (flood_fill(x, y) for (x, y) in lowest)
print(f'Part 2: {mult(sorted(flooded, reverse=True)[:3])}')
