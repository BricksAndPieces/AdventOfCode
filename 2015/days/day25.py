"""
Problem here
"""

from aoc import *

inputs = puzzle_input(25, 2015).split(' ')
code_location = [int(inputs[-3][:-1]), int(inputs[-1][:-1])]


def find_code_num(row, col):
    i = r = c = 1
    while r != row or c != col:
        if r == 1:
            r = c + 1
            c = 1
        else:
            r -= 1
            c += 1

        i += 1

    return i


code_num = find_code_num(code_location[0], code_location[1])

code = 20151125
for _ in range(code_num-1):
    code = (code * 252533) % 33554393

print(f'Part 1: {code}')
print('Part 2: No Part 2. Advent of Code 2015 completed!')
