"""
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2
"""

from aoc import *

inputs = puzzle_input(2, 2022, sample=False).split('\n')
rounds = [a.split(' ') for a in inputs]

p1 = ['A', 'B', 'C']
p2 = ['X', 'Y', 'Z']

def score(round):
    i = p2.index(round[1])
    score = i+1
    if i == p1.index(round[0]):
        score += 3
    elif i == (p1.index(round[0])+1)%3:
        score += 6
    
    return score

ans = sum(score(r) for r in rounds)
print(f'Part 1: {ans}')

def shift(l, n):
    return p2[(p1.index(l)+n)%3]

rounds = [(r[0], shift(r[0], p2.index(r[1])-1)) for r in rounds]
ans = sum(score(r) for r in rounds)
print(f'Part 2: {ans}')
