"""
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1
"""

from aoc import *

name_to_num = {
    'one': '1', 
    'two': '2', 
    'three': '3', 
    'four': '4', 
    'five': '5',
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9'
}

inputs = puzzle_input(1, 2023, sample=False).split('\n')

def solve(part):
    def value(line):
        if part == 2:
            for name in name_to_num:
                inject_num = name[0] + name_to_num[name] + name[-1]
                line = line.replace(name, inject_num)

        nums = [c for c in line if c.isnumeric()]
        return int(nums[0] + nums[-1])

    return sum(value(line) for line in inputs)

print(f'Part 1: {solve(1)}')
print(f'Part 2: {solve(2)}')
