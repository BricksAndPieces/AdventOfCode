"""
--- Day 13: Distress Signal ---
https://adventofcode.com/2022/day/13
"""

from functools import cmp_to_key
from aoc import *

inputs = puzzle_input(13, 2022, sample=False).split('\n\n')

pairs = []
for line in inputs:
    a_raw, b_raw = line.split('\n')
    pairs.append([eval(a_raw), eval(b_raw)])

def right_order(l, r):
    if type(l) == type(r) == int:
        return None if l == r else l < r

    elif type(l) == type(r) == list:
        for i in range(len(l)):
            if i == len(r):
                return False
            rec = right_order(l[i], r[i])
            if rec is not None:
                return rec
        if len(l) < len(r):
            return True

    elif type(l) == list:
        return right_order(l, [r])
    elif type(r) == list:
        return right_order([l], r)
    
    return None

print(f'Part 1: {sum(i+1 for i, a in enumerate(pairs) if right_order(*a))}')

packets = [[[2]], [[6]]]
for pair in pairs:
    packets += pair

packets.sort(key=cmp_to_key(lambda l,r: -1 if right_order(l, r) else 1))
decoder_key = (packets.index([[2]])+1) * (packets.index([[6]])+1)
print(f'Part 2: {decoder_key}')
