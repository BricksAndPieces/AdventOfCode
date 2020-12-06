"""
Problem here
"""

from aoc import *

inputs = puzzle_input(23, 2015).split('\n')


def computer(a_start):
    registers = [a_start, 0]
    i = 0

    while i < len(inputs):
        parts = inputs[i].split(' ')
        i += 1

        if parts[0] == 'hlf':
            registers[parts[1] == 'b'] //= 2
        elif parts[0] == 'tpl':
            registers[parts[1] == 'b'] *= 3
        elif parts[0] == 'inc':
            registers[parts[1] == 'b'] += 1
        elif parts[0] == 'jmp':
            i += int(parts[1]) - 1
        elif parts[0] == 'jie':
            if not registers[parts[1] == 'b'] % 2:
                i += int(parts[2]) - 1
        elif parts[0] == 'jio':
            if registers[parts[1] == 'b'] == 1:
                i += int(parts[2]) - 1

    return registers[1]


print(f'Part 1: {computer(0)}')
print(f'Part 2: {computer(1)}')
