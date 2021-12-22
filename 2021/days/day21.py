"""
--- Day 21: Dirac Dice ---
https://adventofcode.com/2021/day/21
"""

from collections import Counter
from functools import lru_cache
from aoc import *

inputs = puzzle_input(21, 2021, sample=False).split('\n')
p1_pos, p2_pos = [int(a.split(': ')[1]) for a in inputs]


def move(player, moves):
    return (((player - 1) + moves) % 10) + 1


p1 = p2 = steps = 0
turn = 1
while True:
    if turn == 1:
        p1_pos = move(p1_pos, steps * 3 + 6)
        p1 += p1_pos
        turn = 2
    elif turn == 2:
        p2_pos = move(p2_pos, steps * 3 + 6)
        p2 += p2_pos
        turn = 1

    steps += 3

    if p1 >= 1000 or p2 >= 1000:
        break

print(f'Part 1: {min(p1, p2) * steps}')
dice_combos = Counter({6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1})


@lru_cache
def part2(p1_pos, p2_pos, p1=0, p2=0, turn=1):
    if p1 >= 21 or p2 >= 21:
        return (1, 0) if p1 > p2 else (0, 1)

    p1_win_count = 0
    p2_win_count = 0

    for dice_val, occurrences in dice_combos.items():
        if turn == 1:
            new_pos = move(p1_pos, dice_val)
            p1_sub_wins, p2_sub_wins = part2(new_pos, p2_pos, p1 + new_pos, p2, 2)
        elif turn == 2:
            new_pos = move(p2_pos, dice_val)
            p1_sub_wins, p2_sub_wins = part2(p1_pos, new_pos, p1, p2 + new_pos, 1)

        p1_win_count += p1_sub_wins * occurrences
        p2_win_count += p2_sub_wins * occurrences

    return p1_win_count, p2_win_count


p1_pos, p2_pos = [int(a.split(': ')[1]) for a in inputs]
print(f'Part 2: {max(part2(p1_pos, p2_pos))}')
