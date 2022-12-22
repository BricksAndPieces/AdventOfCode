"""
--- Day 19: Not Enough Minerals ---
https://adventofcode.com/2022/day/19
"""

from functools import lru_cache
import re
from aoc import *

blueprints = dict()
inputs = puzzle_input(19, 2022, sample=False).split('\n')

for line in inputs:
    nums = [int(x) for x in re.findall('[0-9]+', line)]
    blueprints[nums[0]] = {
        4: { 0: nums[1] },
        5: { 0: nums[2] },
        6: { 0: nums[3], 1: nums[4] },
        7: { 0: nums[5], 2: nums[6] }
    }

def purchasable(inventory, cost):
    return all(cost[k] <= inventory[k] for k in cost)
    
def max_geodes(bp, time):
    max_ore = max([bp[4][0], bp[5][0], bp[6][0], bp[7][0]])
    max_clay = bp[6][1]
    max_obs = bp[7][2]

    max_so_far = 0

    @lru_cache(maxsize=None)
    def step(time, inventory, prev_buyable):
        if time == 0:
            return inventory[3]

        # if can build a geode bot every min, just compute num geodes
        if inventory[4] >= bp[7][0] and inventory[6] >= bp[7][2]:
            total = 0
            for i in range(time):
                total += i
            return inventory[3] + inventory[7]*time + total
        
        # if branch is doing worse than existing branches, prune it
        total = 0
        for i in range(time):
            total += i
        theoretical_max = inventory[3] + inventory[7]*time + total
        nonlocal max_so_far
        if theoretical_max <= max_so_far:
            return 0

        could_buy = [robot for robot in bp if purchasable(inventory, bp[robot]) and not prev_buyable[robot-4]]
        prev_buyable = tuple(int(purchasable(inventory, bp[i])) for i in range(4, 8))

        inventory = list(inventory)
        for robot in bp:
            inventory[robot-4] += inventory[robot]
        inventory = tuple(inventory)

        def rec_buy(buy):
            new_inv = list(inventory)
            for k in bp[buy]:
                new_inv[k] -= bp[buy][k]
            
            new_inv[buy] += 1

            return step(time-1, tuple(new_inv), (0,0,0,0))
        
        max_result = 0
        if 7 in could_buy:
            max_result = max(max_result, rec_buy(7))
        else:
            for buy in could_buy:
                # don't need more than max_ore ore machines
                if buy == 4 and inventory[4] >= max_ore:
                    continue
                # don't need more than max_clay clay machines
                if buy == 5 and inventory[5] >= max_clay:
                    continue
                # don't need more than max_obs machines
                if buy == 6 and inventory[6] >= max_obs:
                    continue
                max_result = max(max_result, rec_buy(buy))
        
        max_result = max(max_result, step(time-1, inventory, prev_buyable))

        max_so_far = max(max_so_far, max_result)
        return max_result

    inventory = (0, 0, 0, 0, 1, 0, 0, 0)
    prev_buyable = (0, 0, 0, 0)
    return step(time, inventory, prev_buyable)

quality_levels = []
@timeit
def solve_1():
    for n in range(1, len(blueprints)+1):
        geodes = max_geodes(blueprints[n], 24)
        quality_levels.append(n * geodes)
solve_1()
    
print(f'Part 1: {sum(quality_levels)}')

num_geodes = []
@timeit
def solve_2():
    for n in range(1, min(4, len(blueprints)+1)):
        geodes = max_geodes(blueprints[n], 32)
        num_geodes.append(geodes)
solve_2()

print(f'Part 2: {mult(num_geodes)}')
