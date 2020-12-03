"""
Problem goes here
"""

from aoc import *
from itertools import permutations


def int_code(program, phase, code_input):
    phase_inputted = False
    i = 0
    while program[i] != 99:
        instruction = f'{program[i]:05}'
        op = int(instruction[3:])
        params = [int(s) for s in instruction[:3]]

        mode_a, mode_b, mode_c = params
        args = []
        if op in [1, 2, 4, 5, 6, 7, 8]:
            if mode_c == 0:
                args.append(program[program[i + 1]])
            else:
                args.append(program[i + 1])

            if op in [1, 2, 5, 6, 7, 8]:
                if mode_b == 0:
                    args.append(program[program[i + 2]])
                else:
                    args.append(program[i + 2])

                if op in []:
                    if mode_a == 0:
                        args.append(program[program[i + 3]])
                    else:
                        args.append(program[i + 3])

        if op == 1:
            program[program[i + 3]] = args[0] + args[1]
            i += 4
        elif op == 2:
            program[program[i + 3]] = args[0] * args[1]
            i += 4
        elif op == 3:
            program[program[i + 1]] = code_input if phase_inputted else phase
            phase_inputted = True
            i += 2
        elif op == 4:
            return args[0]
            # i += 2
        elif op == 5:
            i = args[1] if args[0] else i + 3
        elif op == 6:
            i = args[1] if not args[0] else i + 3
        elif op == 7:
            program[program[i + 3]] = 1 if args[0] < args[1] else 0
            i += 4
        elif op == 8:
            program[program[i + 3]] = 1 if args[0] == args[1] else 0
            i += 4
        else:
            print(f'Something went wrong: Opcode {op}')


def part1(inputs):
    max_thrust = 0
    phases = permutations([0, 1, 2, 3, 4])
    for phase in phases:
        code_input = 0

        for i in phase:
            program = inputs.copy()
            code_input = int_code(program, i, code_input)

        max_thrust = max(max_thrust, code_input)

    return max_thrust


def part2(inputs):
    pass


puzzle_input = ints(puzzle_input(7, 2019), ',')
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
