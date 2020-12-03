"""
Problem goes here
"""

from aoc import *


def part1(inputs):
    x = 0
    count = 0
    for i in inputs:
        if i[x % len(i)] == '#':
            count += 1
        x += 3

    return count


def part2(inputs):
    z = [1, 3, 5, 7]
    trees = 1
    for y in z:
        x = 0
        count = 0
        for i in inputs:
            if i[x % len(i)] == '#':
                count += 1
            x += y

        trees *= count

    x = 0
    count = 0
    for i in range(0, len(inputs), 2):
        if inputs[i][x % len(inputs[i])] == '#':
            count += 1
        x += 1

    return trees * count


puzzle_input = puzzle_input(3).split('\n')
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
