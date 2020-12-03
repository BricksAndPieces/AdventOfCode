"""
Problem goes here
"""

from aoc import *


def part1(inputs):
    x, y = 0, 0
    houses = set()
    for d in inputs:
        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '<' :
            x -= 1
        elif d == '>':
            x += 1

        houses.add((x, y))

    return len(houses)


def part2(inputs):
    x, y = 0, 0
    rx, ry = 0, 0
    houses = set()
    real = True

    for d in inputs:
        if real:
            if d == '^':
                y += 1
            elif d == 'v':
                y -= 1
            elif d == '<':
                x -= 1
            elif d == '>':
                x += 1

            houses.add((x, y))
        else:
            if d == '^':
                ry += 1
            elif d == 'v':
                ry -= 1
            elif d == '<':
                rx -= 1
            elif d == '>':
                rx += 1

            houses.add((rx, ry))

        real ^= True

    return len(houses)


puzzle_input = puzzle_input(3, 2015)
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
