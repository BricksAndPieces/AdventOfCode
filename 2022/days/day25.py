"""
--- Day 25: Full of Hot Air ---
https://adventofcode.com/2022/day/25
"""

from aoc import *

decode = { '=': -2, '-': -1, '0': 0, '1': 1, '2': 2 }
def snafu_to_decimal(s): 
    return sum(decode[d] * 5**i for i, d in enumerate(reversed(s)))

encode = '012=-'
def decimal_to_snafu(n):
    s = ''
    while n != 0:
        s = encode[n % 5] + s
        n = (n+2) // 5
    return s
            
inputs = puzzle_input(25, 2022, sample=False).split('\n')
decimal_sum = sum(snafu_to_decimal(line) for line in inputs)
snafu_sum = decimal_to_snafu(decimal_sum)

print(f'Part 1: {snafu_sum}')
