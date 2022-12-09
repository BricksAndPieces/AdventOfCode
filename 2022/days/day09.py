"""
--- Day 9: Rope Bridge ---
https://adventofcode.com/2022/day/9
"""

from aoc import *

inputs = puzzle_input(9, 2022, sample=False).split('\n')
inputs = [(a[0], int(a[2:])) for a in inputs]

dirs = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

num_knots = 10
knots = [[0, 0] for _ in range(num_knots)]
part1, part2 = [], []

for d, n in inputs:
    for _ in range(n):
        knots[0][0] += dirs[d][0]
        knots[0][1] += dirs[d][1]

        for i in range(1, num_knots):
            dx, dy = knots[i][0] - knots[i-1][0], knots[i][1] - knots[i-1][1]
            if abs(dx) > 1 or abs(dy) > 1:
                dx = max(-1, min(1, dx))
                dy = max(-1, min(1, dy))
                knots[i][0] -= dx
                knots[i][1] -= dy

        part1.append(tuple(knots[1]))
        part2.append(tuple(knots[-1]))

print(f'Part 1: {len(set(part1))}')
print(f'Part 2: {len(set(part2))}')
