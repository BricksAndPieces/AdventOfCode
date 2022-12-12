"""
--- Day 12: Hill Climbing Algorithm ---
https://adventofcode.com/2022/day/12
"""

from dataclasses import dataclass
from aoc import *

@dataclass
class Square:
    height: int
    score: int = 99999999999

grid = []
S = None
E = None

inputs = puzzle_input(12, 2022, sample=False).split('\n')
for x, line in enumerate(inputs):
    grid.append([])
    for y, letter in enumerate(line):
        if letter == 'S':
            S = (x, y)
            letter = 'a'
        if letter == 'E':
            E = (x, y)
            letter = 'z'
        grid[-1].append(Square(ord(letter)))

grid[E[0]][E[1]].score = 0
queue = [E]

while queue:
    x, y = queue.pop(0)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        px = x + dx
        py = y + dy
        if px < 0 or px >= len(grid) or py < 0 or py >= len(grid[0]):
            continue

        if (grid[px][py].height+1) >= grid[x][y].height:
            if grid[px][py].score > (grid[x][y].score+1):
                grid[px][py].score = grid[x][y].score + 1
                queue.append((px, py))


print(f'Part 1: {grid[S[0]][S[1]].score}')

a_coords = (
    (x, y) 
    for x in range(len(grid)) 
    for y in range(len(grid[0])) 
    if grid[x][y].height == ord('a')
)
min_path = min(grid[a[0]][a[1]].score for a in a_coords)
print(f'Part 2: {min_path}')
