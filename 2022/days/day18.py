"""
--- Day 18: Boiling Boulders ---
https://adventofcode.com/2022/day/18
"""

from collections import deque
from aoc import *

inputs = puzzle_input(18, 2022, sample=False).split('\n')
cubes = set(tuple(ints(a, ',')) for a in inputs)

def add(t1, t2):
        return tuple(t1+t2 for t1, t2 in zip(t1, t2))

def count_faces(shape):
    total = 0
    for c in shape:
        for d in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            if add(c, d) not in shape:
                total += 1

    return total

print(f'Part 1: {count_faces(cubes)}')

min_x, max_x = min(a[0] for a in cubes), max(a[0] for a in cubes)
min_y, max_y = min(a[1] for a in cubes), max(a[1] for a in cubes)
min_z, max_z = min(a[2] for a in cubes), max(a[2] for a in cubes)

def in_bounds(c):
    return min_x-2 < c[0] < max_x+2 and min_y-2 < c[1] < max_y+2 and min_z-2 < c[2] < max_z+2

steam = set()
start = (min_x-1, min_y-1, min_z-1)
q = deque([start])

while q:
    c = q.pop()
    for d in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
        new_cube = add(c, d)
        if in_bounds(new_cube) and new_cube not in steam and new_cube not in cubes:
            steam.add(new_cube)
            q.append(new_cube)

x = max_x - min_x + 3
y = max_y - min_y + 3
z = max_z - min_z + 3

exterior_steam = x*y*2 + x*z*2 + y*z*2
exterior_cubes = count_faces(steam) - exterior_steam
print(f'Part 2: {exterior_cubes}')
