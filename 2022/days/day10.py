"""
--- Day 10: Cathode-Ray Tube ---
https://adventofcode.com/2022/day/10
"""

from aoc import *

inputs = puzzle_input(10, 2022, sample=False).split('\n')

x = 1
tick = 0
signals = []
crt = []

def cycle(tick):
    draw = tick%40 in [x-1, x, x+1]
    crt.append('\u2588' if draw else ' ')
    signals.append((tick+1) * x)
    return tick + 1

for line in inputs:
    tick = cycle(tick)
    instruct = line.split(' ')
    if instruct[0] == 'addx':
        tick = cycle(tick)
        x += int(instruct[1])
        
print(f'Part 1: {sum(signals[19::40])}')

print('Part 2:')
for i in range(6):
    print(''.join(crt[i*40:(i+1)*40]))
