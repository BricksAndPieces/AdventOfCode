"""
--- Day 10: Syntax Scoring ---
https://adventofcode.com/2021/day/10
"""

from aoc import *

inputs = puzzle_input(10, 2021, sample=True).split('\n')

bracket_map = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}


def eval_brackets(line):
    stack = []
    for c in line:
        if c in ['(', '{', '[', '<']:
            stack.append(c)
        elif c in [')', '}', ']', '>']:
            if stack and stack[-1] == bracket_map[c]:
                stack.pop()
            else:
                return False, c, stack

    return True, None, stack


part1_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

part1 = [eval_brackets(line) for line in inputs]
part1 = sum(part1_points[brack] for (valid, brack, _) in part1 if not valid)
print(f'Part 1: {part1}')

part2_points = [
    reduce(
        lambda a, b: a * 5 + '_([{<'.index(b),  # _ is a placeholder
        reversed(eval_brackets(line)[2]), 0
    )
    for line in inputs if eval_brackets(line)[0]
]

print(f'Part 2: {[*sorted(part2_points)][len(part2_points)//2]}')
