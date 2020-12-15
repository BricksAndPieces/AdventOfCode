"""
Problem here
"""

from itertools import combinations, permutations, product
from functools import lru_cache
import numpy as np
import re

from collections import defaultdict
from aoc import *


class Computer:

    def __init__(self, program):
        self.program = defaultdict(lambda x: 0)
        for i, n in enumerate(program):
            self.program[i] = n

        self.index = 0
        self.halted = False
        self.relative_base = 0

    def get_args(self):
        # Parameter Modes:
        # 0 - Position Mode
        # 1 - Immediate Mode
        # 2 - Relative Mode

        instruction = f'{self.program[self.index]:05}'
        op = int(instruction[3:])
        params = [int(s) for s in instruction[:3]]

        mode_a, mode_b, mode_c = params
        args = []

        if op in [1, 2, 4, 5, 6, 7, 8, 9]:
            if mode_c == 0:
                args.append(self.program[self.program[self.index + 1]])
            elif mode_c == 1:
                args.append(self.program[self.index + 1])
            elif mode_c == 2:
                args.append(self.program[self.relative_base + self.program[self.index + 1]])

        if op in [1, 2, 5, 6, 7, 8]:
            if mode_b == 0:
                args.append(self.program[self.program[self.index + 2]])
            elif mode_b == 1:
                args.append(self.program[self.index + 2])
            elif mode_b == 2:
                args.append(self.program[self.relative_base + self.program[self.index + 2]])

        if op in []:
            if mode_a == 0:
                args.append(self.program[self.program[self.index + 3]])
            elif mode_a == 1:
                args.append(self.program[self.index + 3])
            elif mode_a == 2:
                args.append(self.program[self.relative_base + self.program[self.index + 3]])

        offset = 0
        if op in [1, 2, 7, 8] and mode_a == 2:
            offset = self.relative_base

        if op in [3] and mode_c:
            offset = self.relative_base


        return op, args, offset

    def output(self, code_input):
        while self.program[self.index] != 99:
            op, args, offset = self.get_args()
            if op == 1:
                self.program[self.program[self.index + 3] + offset] = args[0] + args[1]
                self.index += 4
            elif op == 2:
                self.program[self.program[self.index + 3] + offset] = args[0] * args[1]
                self.index += 4
            elif op == 3:
                self.program[self.program[self.index + 1] + offset] = code_input
                self.index += 2
            elif op == 4:
                self.index += 2
                return args[0]
            elif op == 5:
                self.index = args[1] if args[0] else self.index + 3
            elif op == 6:
                self.index = args[1] if not args[0] else self.index + 3
            elif op == 7:
                self.program[self.program[self.index + 3] + offset] = 1 if args[0] < args[1] else 0
                self.index += 4
            elif op == 8:
                self.program[self.program[self.index + 3] + offset] = 1 if args[0] == args[1] else 0
                self.index += 4
            elif op == 9:
                self.relative_base += args[0]
                self.index += 2
            else:
                print(self.program)
                raise Exception(f'Invalid Opcode: {op}')

        self.halted = True


inputs = ints(puzzle_input(9, 2019), ',')
comp = Computer(inputs.copy())
print(f'Part 1: {comp.output(1)}')

comp = Computer(inputs.copy())
print(f'Part 2: {comp.output(2)}')
