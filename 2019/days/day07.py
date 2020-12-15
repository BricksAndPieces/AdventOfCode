"""
Problem goes here
"""

from aoc import *
from itertools import permutations


class Computer:
    def __init__(self, program, phase):
        self.program = program
        self.phase = phase
        self.phase_inputted = False
        self.index = 0
        self.halted = False

    def get_args(self):
        instruction = f'{self.program[self.index]:05}'
        op = int(instruction[3:])
        params = [int(s) for s in instruction[:3]]

        mode_a, mode_b, mode_c = params
        args = []
        if op in [1, 2, 4, 5, 6, 7, 8]:
            if mode_c == 0:
                args.append(self.program[self.program[self.index + 1]])
            else:
                args.append(self.program[self.index + 1])

            if op in [1, 2, 5, 6, 7, 8]:
                if mode_b == 0:
                    args.append(self.program[self.program[self.index + 2]])
                else:
                    args.append(self.program[self.index + 2])

                if op in []:
                    if mode_a == 0:
                        args.append(self.program[self.program[self.index + 3]])
                    else:
                        args.append(self.program[self.index + 3])

        return op, args

    def output(self, code_input):
        while self.program[self.index] != 99:
            op, args = self.get_args()
            if op == 1:
                self.program[self.program[self.index + 3]] = args[0] + args[1]
                self.index += 4
            elif op == 2:
                self.program[self.program[self.index + 3]] = args[0] * args[1]
                self.index += 4
            elif op == 3:
                self.program[self.program[self.index + 1]] = code_input if self.phase_inputted else self.phase
                self.phase_inputted = True
                self.index += 2
            elif op == 4:
                self.index += 2
                return args[0]
            elif op == 5:
                self.index = args[1] if args[0] else self.index + 3
            elif op == 6:
                self.index = args[1] if not args[0] else self.index + 3
            elif op == 7:
                self.program[self.program[self.index + 3]] = 1 if args[0] < args[1] else 0
                self.index += 4
            elif op == 8:
                self.program[self.program[self.index + 3]] = 1 if args[0] == args[1] else 0
                self.index += 4
            else:
                print(self.program)
                raise Exception(f'Invalid Opcode: {op}')

        self.halted = True


def part1(inputs):
    max_thrust = 0
    phases = permutations([0, 1, 2, 3, 4])
    for phase in phases:
        code_input = 0

        for i in phase:
            program = inputs.copy()
            comp = Computer(program, i)
            code_input = comp.output(code_input)

        max_thrust = max(max_thrust, code_input)

    return max_thrust


def part2(inputs):
    max_thrust = 0
    phases = permutations([5, 6, 7, 8, 9])
    for phase in phases:
        code_input = 0
        comps = [Computer(inputs.copy(), i) for i in phase]

        while not comps[0].halted:
            for comp in comps:
                val = comp.output(code_input)
                if val is not None:
                    code_input = val

        max_thrust = max(max_thrust, code_input)

    return max_thrust


puzzle_input = ints(puzzle_input(7, 2019), ',')
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
