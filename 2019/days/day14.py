"""
Problem here
"""

from itertools import combinations, permutations, product
from functools import lru_cache
import numpy as np
import re

from aoc import *


def ore_count(chemical):
    pass


inputs = puzzle_input(14, 2019, sample=True).split('\n')

chemical_map = {}
for line in inputs:
    space_split = line.split(' ')
    key = space_split[-1]
    amount = int(space_split[-2])



print(f'Part 1: {0}')
print(f'Part 2: {0}')
