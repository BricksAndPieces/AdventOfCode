"""
--- Day 24: {PUZZLE NAME HERE} ---
https://adventofcode.com/2021/day/24
"""

from collections import defaultdict, deque
from itertools import combinations, permutations, product
from functools import lru_cache, reduce
import numpy as np
import re

from aoc import *

inputs = [a.split(' ') for a in puzzle_input(24, 2021, sample=False).split('\n')]
constants = [[4 + 18 * n, 5 + 18 * n, 15 + 18 * n] for n in range(14)]
constants = [[int(inputs[z][2]) for z in a] for a in constants]

levels = {}
def build_deps(i, zl):
    A, B, C = constants[i]

    sols = defaultdict(list)
    for w in range(9, 0, -1):
        for z in zl:
            for a in range(A):
                pz = z * A + a
                if pz % 26 + B == w:
                    if pz // A == z:
                        sols[pz].append((w, z))

                pz = round((z - w - C) / 26 * A + a)
                if pz % 26 + B != w:
                    if pz//A * 26 + w + C == z:
                        sols[pz].append((w, z))

    assert sols
    levels[i] = sols

    if i > 0:
        build_deps(i-1, list(sols.keys()))

p1 = None
p2 = None
def solve(i, z, sol, largest=False):
    global p1, p2

    if i == 14:
        if largest:
            p1 = ''.join(str(j) for j in sol)
        else:
            p2 = ''.join(str(j) for j in sol)
        return True

    if z not in levels[i]:
        return False

    for w, nz in sorted(levels[i][z], reverse=largest):
        ts = (*sol, w)
        if solve(i+1, nz, list(ts), largest):
            return True


build_deps(13, [0])
solve(0, 0, [], largest=True)
solve(0, 0, [], largest=False)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
