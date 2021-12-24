"""
--- Day 22: Reactor Reboot ---
https://adventofcode.com/2021/day/22
"""

from aoc import *

inputs = puzzle_input(22, 2021, sample=False).split('\n')
inputs = [[z for z in a.split(' ')] for a in inputs]
inputs = [[*[[int((x := z.split('..'))[0][2:]), int(x[1]) + 1] for z in a[1].split(',')], a[0] == 'on'] for a in inputs]
inputs = [[x1, x2, y1, y2, z1, z2, s] for [[x1, x2], [y1, y2], [z1, z2], s] in inputs]


def solve(part1):
    cubes = []
    for [x1, x2, y1, y2, z1, z2, state] in inputs:
        if part1 and (x2 < -50 or x1 > 50 or y2 < -50 or y1 > 50 or z2 < -50 or z1 > 50):
            continue

        new_cubes = []
        for c in cubes:
            x_overlaps = x2 > c[0] and x1 < c[1]
            y_overlaps = y2 > c[2] and y1 < c[3]
            z_overlaps = z2 > c[4] and z1 < c[5]

            if x_overlaps and y_overlaps and z_overlaps:
                if c[0] < x1:
                    new_c = c.copy()
                    new_c[1] = x1
                    c[0] = x1
                    new_cubes.append(new_c)
                if c[1] > x2:
                    new_c = c.copy()
                    new_c[0] = x2
                    c[1] = x2
                    new_cubes.append(new_c)
                if c[2] < y1:
                    new_c = c.copy()
                    new_c[3] = y1
                    c[2] = y1
                    new_cubes.append(new_c)
                if c[3] > y2:
                    new_c = c.copy()
                    new_c[2] = y2
                    c[3] = y2
                    new_cubes.append(new_c)
                if c[4] < z1:
                    new_c = c.copy()
                    new_c[5] = z1
                    c[4] = z1
                    new_cubes.append(new_c)
                if c[5] > z2:
                    new_c = c.copy()
                    new_c[4] = z2
                    c[5] = z2
                    new_cubes.append(new_c)

            else:
                new_cubes.append(c)

        new_cubes.append([x1, x2, y1, y2, z1, z2, state])
        cubes = new_cubes

    return sum((x2 - x1) * (y2 - y1) * (z2 - z1) for x1, x2, y1, y2, z1, z2, s in cubes if s)


print(f'Part 1: {solve(True)}')
print(f'Part 2: {solve(False)}')
