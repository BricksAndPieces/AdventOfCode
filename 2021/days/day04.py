"""
--- Day 4: Giant Squid ---
https://adventofcode.com/2021/day/4
"""

from dataclasses import dataclass
from aoc import *


@dataclass
class BingoElement:
    num: int
    marked: bool = False


class Board:
    def __init__(self, board_nums):
        self.content = [[BingoElement(element) for element in line] for line in board_nums]

    def is_completed(self):
        return any(all(el.marked for el in line) for line in self.content + [*zip(*self.content[::-1])])

    def mark_num(self, num):
        for line in self.content:
            for el in line:
                if el.num == num:
                    el.marked = True

    def sum_unmarked(self):
        return sum(sum((0 if el.marked else el.num) for el in line) for line in self.content)


inputs = puzzle_input(4, 2021, sample=False).split('\n')
rng_nums = [int(a) for a in inputs[0].split(',')]

boards = '\n'.join(inputs[2:]).split('\n\n')
boards = [[[int(n) for n in line.lstrip().replace('  ', ' ').split(' ')] for line in b.split('\n')] for b in boards]
boards = [Board(b) for b in boards]

part1 = True
for n in rng_nums:
    for b in boards:
        b.mark_num(n)
        if part1 and b.is_completed():
            print(f'Part 1: {n * b.sum_unmarked()}')
            part1 = False

    if len(boards) == 1 and boards[0].is_completed():
        print(f'Part 2: {n * boards[0].sum_unmarked()}')

    boards = [b for b in boards if not b.is_completed()]
