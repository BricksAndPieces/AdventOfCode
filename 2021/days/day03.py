"""
--- Day 3: Binary Diagnostic ---
https://adventofcode.com/2021/day/3
"""

from operator import lt, ge
from functools import partial
from aoc import *

inputs = puzzle_input(3, 2021, sample=False).split('\n')


def bit_count(lst):
    n0 = [0] * len(lst[0])
    n1 = [0] * len(lst[0])
    for line in lst:
        for n, e in enumerate(line):
            if e == '0':
                n0[n] += 1
            else:
                n1[n] += 1

    return n0, n1


num_0s, num_1s = bit_count(inputs)
gamma = ''.join(['0' if a > b else '1' for (a, b) in zip(num_0s, num_1s)])
epsilon = ''.join(['0' if a < b else '1' for (a, b) in zip(num_0s, num_1s)])
print(f'Part 1: {int(gamma, 2) * int(epsilon, 2)}')


def filter_bits(lst, f):
    for x in range(len(lst[0])):
        n0, n1 = bit_count(lst)
        lst = [a for a in lst if f(a, x, n0, n1)]
        if len(lst) == 1:
            break

    return lst[0]


def filter_func(oper, a, n, n0, n1):
    return a[n] == ('1' if oper(n1[n], n0[n]) else '0')


o2 = int(filter_bits(inputs.copy(), partial(filter_func, ge)), 2)
co2 = int(filter_bits(inputs.copy(), partial(filter_func, lt)), 2)
print(f'Part 2: {co2 * o2}')
