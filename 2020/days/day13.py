"""
Problem here
"""

from aoc import *

inputs = puzzle_input(13, 2020).split('\n')
timestamp = int(inputs[0])
bus_ids = [int(s) for s in inputs[1].split(',') if s.isdigit()]

wait_time = [-(timestamp % x) + x for x in bus_ids]
min_wait = min(wait_time)
min_bus = bus_ids[wait_time.index(min_wait)]

print(f'Part 1: {min_wait * min_bus}')

# Chinese Remainder Theorem - Search by Sieving
buses = [(int(b), ((int(b) - n) % int(b))) for n, b in enumerate(inputs[1].split(',')) if b.isdigit()]

b, t = buses[0]
for db, dt in buses[1:]:
    while True:
        t += b
        if t % db == dt:
            break

    b *= db

print(f'Part 2: {t}')
