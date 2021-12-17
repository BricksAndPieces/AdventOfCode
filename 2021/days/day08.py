"""
--- Day 8: Seven Segment Search ---
https://adventofcode.com/2021/day/8
"""

from itertools import permutations
from aoc import *

inputs = puzzle_input(8, 2021, sample=False).split('\n')
inputs = [a.split(' | ') for a in inputs]
inputs = [(a[0].split(' '), a[1].split(' ')) for a in inputs]

part1 = sum(sum(len(o) in (2, 3, 4, 7) for o in outputs) for (_, outputs) in inputs)
print(f'Part 1: {part1}')


def decode(segments, turned_on):
    segment_defs = (
        (0, 1, 2, 4, 5, 6),     # 0
        (2, 5),                 # 1
        (0, 2, 3, 4, 6),        # 2
        (0, 2, 3, 5, 6),        # 3
        (1, 2, 3, 5),           # 4
        (0, 1, 3, 5, 6),        # 5
        (0, 1, 3, 4, 5, 6),     # 6
        (0, 2, 5),              # 7
        (0, 1, 2, 3, 4, 5, 6),  # 8
        (0, 1, 2, 3, 5, 6),     # 9
    )

    for i, seg_def in enumerate(segment_defs):
        # Returns the index (decoded number) if the segments match exactly
        if all((n in seg_def) == (segments[n] in turned_on) for n in range(7)):
            return i

    return -1


def part2(test_data, outputs):
    for perm in permutations('abcdefg', r=7):
        correct = True
        decoded = {}
        for test in test_data:
            d = decode(''.join(perm), test)
            if d == -1 or d in decoded:
                correct = False
                break
            else:
                decoded[d] = ''.join(sorted(test))

        if not correct:
            continue

        # Reverse the orientation of the dictionary
        decoded = {v: k for (k, v) in decoded.items()}
        digits = [decoded[''.join(sorted(a))] for a in outputs]
        return digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]


print(f'Part 2: {sum(part2(a[0], a[1]) for a in inputs)}')
