"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1
"""

from aoc import *

inputs = ints(puzzle_input(1, 2021, sample=False))
solution = lambda l: sum(e < l[n + 1] for n, e in enumerate(l[:-1]))
print(f'Part 1: {solution(inputs)}')

triples = [e + inputs[n + 1] + inputs[n + 2] for n, e in enumerate(inputs[:-2])]
print(f'Part 2: {solution(triples)}')
