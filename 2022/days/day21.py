"""
--- Day 21: Monkey Math ---
https://adventofcode.com/2022/day/21
"""

from aoc import *

inputs = puzzle_input(21, 2022, sample=False).split('\n')
monkeys = {}
for line in inputs:
    parts = line.split(': ')
    if parts[1].isdigit():
        monkeys[parts[0]] = int(parts[1])
    else:
        monkeys[parts[0]] = parts[1].split(' ')

def solve_1(key):
    eq = monkeys[key]
    if type(eq) is int:
        return eq

    a = solve_1(eq[0])
    b = solve_1(eq[2])
    return int(eval(f'{a}{eq[1]}{b}'))

print(f'Part 1: {solve_1("root")}')

def simplify(key):
    if key == 'humn':
        return 'humn'

    eq = monkeys[key]
    if type(eq) is int:
        return eq
    
    a = simplify(eq[0])
    b = simplify(eq[2])

    if key == 'root':
        return (a, '=', b)

    if type(a) == type(b) == int:
        return int(eval(f'{a}{eq[1]}{b}'))

    return (a, eq[1], b)

def solve_2(eq):
    if eq[0] == 'humn':
        return eq[2]
    if eq[2] == 'humn':
        return eq[0]

    sub = eq[2] if type(eq[0]) is int else eq[0]
    num = eq[0] if type(eq[0]) is int else eq[2]

    if type(sub[0]) is int:
        if sub[1] == '+':
            return solve_2((num - sub[0], '=', sub[2]))
        if sub[1] == '-':
            return solve_2(((num, '+', sub[2]), '=', sub[0]))
        if sub[1] == '*':
            return solve_2((num // sub[0], '=', sub[2]))
        if sub[1] == '-':
            return solve_2(((num, '*', sub[2]), '=', sub[0]))
    else:
        if sub[1] == '+':
            return solve_2((num - sub[2], '=', sub[0]))
        if sub[1] == '-':
            return solve_2((num + sub[2], '=', sub[0]))
        if sub[1] == '*':
            return solve_2((num // sub[2], '=', sub[0]))
        if sub[1] == '/':
            return solve_2((num * sub[2], '=', sub[0]))
    
print(f'Part 2: {solve_2(simplify("root"))}')
