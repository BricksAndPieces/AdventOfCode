"""
--- Day 18: Snailfish ---
https://adventofcode.com/2021/day/18
"""

from collections import defaultdict, deque
from itertools import combinations, permutations, product
from functools import lru_cache, reduce
import numpy as np
import re
import math

from aoc import *

inputs = puzzle_input(18, 2021, sample=True).split('\n')
assert all(re.match('^[\[\],0123456789]+$', a) for a in inputs)
inputs = [eval(a) for a in inputs]

print(inputs)


def add(n1, n2):
    return [n1, n2]


def split(n):  # Returns number and whether a change was made
    if isinstance(n, int):
        if n >= 10:
            return [n//2, math.ceil(n/2)], True
        return n, False

    left, change = split(n[0])
    if change:
        return [left, n[1]], True

    right, change = split(n[0])
    return [n[0], right], change


def explode(n):
    pass


def reduce_snailfish(number, depth=1):
    if isinstance(number, int):
        return split(number) if number >= 10 else number

    number[0] = reduce_snailfish(number[0], depth+1)
    number[1] = reduce_snailfish(number[1], depth+1)

    return number





ex = [[[[[4,3],4],4],[7,[[50,4],9]]],[1,1]]

print(ex)
print(reduce_snailfish(ex))



def mag(n):
    return n if isinstance(n, int) else 3 * mag(n[0]) + 2 * mag(n[1])




print(f'Part 1: {0}')
print(f'Part 2: {0}')
