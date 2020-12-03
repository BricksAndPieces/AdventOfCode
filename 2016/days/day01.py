"""
--- Day 1: No Time for a Taxicab ---
Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by
stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve
all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can
get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to
work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then,
follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of
blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the
destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the
destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

--- Part Two ---
Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the
first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

from aoc import *


def part1(inputs):
    x, y = 0, 0
    d = 1
    for i in inputs:
        if i[0] == 'L':
            d -= 1
            if d == 0:
                d = 4
        else:
            d += 1
            if d == 5:
                d = 1

        a = int(i[1:])
        if d == 1:
            y += a
        elif d == 2:
            x += a
        elif d == 3:
            y -= a
        else:
            x -= a

    return abs(x) + abs(y)


def part2(inputs):
    locs = []
    x, y = 0, 0
    d = 1
    for i in inputs:
        if i[0] == 'L':
            d -= 1
            if d == 0:
                d = 4
        else:
            d += 1
            if d == 5:
                d = 1

        for _ in range(int(i[1:])):
            if d == 1:
                y += 1
            elif d == 2:
                x += 1
            elif d == 3:
                y -= 1
            else:
                x -= 1

            if (x, y) in locs:
                return abs(x) + abs(y)

            locs.append((x, y))


puzzle_input = [s.strip() for s in puzzle_input(1, 2016).split(',')]
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
