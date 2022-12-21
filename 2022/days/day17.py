"""
--- Day 17: Pyroclastic Flow ---
https://adventofcode.com/2022/day/17
"""

from aoc import *

falling_rocks = [
    [0b0011110],
    [0b0001000,0b0011100,0b0001000],
    [0b0000100,0b0000100,0b0011100],
    [0b0010000,0b0010000,0b0010000,0b0010000],
    [0b0011000,0b0011000]
]

def find_lcm(a, b):
    n1, n2 = a, b
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return a * b // n1

@timeit
def solve(n, sample):
    jet_inc, rock_inc = 0, 0
    jets = puzzle_input(17, 2022, sample=sample)
    layers = [0b1111111]
    heights = []
    lcm = find_lcm(len(falling_rocks), len(jets))

    for _ in range(lcm * 3 - 1):
        rock = falling_rocks[rock_inc]
        rock_inc = (rock_inc + 1) % len(falling_rocks)
        rock_y = len(layers) + len(rock) + 2

        while True:
            jet = jets[jet_inc]
            jet_inc = (jet_inc + 1) % len(jets)

            for dy in range(len(rock)):
                if rock[dy] >> 6 and jet == '<':
                    break
                if rock[dy] % 2 and jet == '>':
                    break

                new_rock = rock[dy] << 1 if jet == '<' else rock[dy] >> 1
                if rock_y-dy < len(layers) and new_rock & layers[rock_y-dy]:
                    break
            else:
                rock = [x << 1 if jet == '<' else x >> 1 for x in rock]

            stop_falling = False
            for dy in range(len(rock)):
                if rock_y-dy <= len(layers):
                    if rock[dy] & layers[rock_y-dy-1]:
                        stop_falling = True
                        break
            
            if stop_falling:
                height_added = 0
                for dy in reversed(range(len(rock))):
                    if rock_y-dy < len(layers):
                        layers[rock_y-dy] |= rock[dy]
                    else:
                        height_added += 1
                        layers.append(rock[dy])
                    
                heights.append(height_added)
                break

            rock_y -= 1

    repeat = None
    for c in reversed(range(len(heights)//2)):
        if heights[-c:] == heights[-2*c:-c]:
            repeat = heights[-c:]
            break
    
    n_repeats = n // len(repeat)
    return sum(heights[:n - n_repeats * len(repeat)]) + (sum(repeat) * n_repeats)

sample = False
print(f'Part 1: {solve(2022, sample)}')
print(f'Part 2: {solve(1_000_000_000_000, sample)}')
