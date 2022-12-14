"""
--- Day 14: Regolith Reservoir ---
https://adventofcode.com/2022/day/14
"""

from collections import defaultdict
from aoc import *

inputs = puzzle_input(14, 2022, sample=False).split('\n')
grid = defaultdict(lambda: '.')

for line in inputs:
    coords = line.split(' -> ')
    for i in range(len(coords)-1):
        from_x, from_y = ints(coords[i], ',')
        to_x, to_y = ints(coords[i+1], ',')

        if from_x != to_x:
            l, r = min(from_x, to_x), max(from_x, to_x) + 1
            for x in range(l, r):
                grid[(x, from_y)] = '#'
        else:
            l, r = min(from_y, to_y), max(from_y, to_y) + 1
            for y in range(l, r):
                grid[(from_x, y)] = '#'

lowest_rock = max(a[1] for a in grid.keys() if grid[a] == '#')

abyss_sand = 0
total_sand = 0
part2 = False

break_loop = False
while not break_loop:
    sand = (500, 0)

    while True:
        if grid[(sand[0], sand[1]+1)] == '.':
            sand = (sand[0], sand[1]+1)
        elif grid[(sand[0]-1, sand[1]+1)] == '.':
            sand = (sand[0]-1, sand[1]+1)
        elif grid[(sand[0]+1, sand[1]+1)] == '.':
            sand = (sand[0]+1, sand[1]+1)
        else:
            total_sand += 1
            grid[sand] = 'o'
            if sand == (500, 0):
                break_loop = True
            break

        if sand[1] == lowest_rock and abyss_sand == 0:
            abyss_sand = total_sand
            part2 = True
                    
        if sand[1] == lowest_rock+1:
            grid[sand] = 'o'
            total_sand += 1
            break


print(f'Part 1: {abyss_sand}')
print(f'Part 2: {total_sand}')
