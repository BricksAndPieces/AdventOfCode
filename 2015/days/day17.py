"""
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move
it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are
four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

--- Part Two ---
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving
department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you
fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and
so the answer there would be 3.
"""

from aoc import *
from itertools import combinations

inputs = ints(puzzle_input(17, 2015))
result = [seq for i in range(len(inputs), 0, -1) for seq in combinations(inputs, i) if sum(seq) == 150]
ans1 = len(result)

container_num = sorted([len(x) for x in result])
ans2 = 0
while container_num[ans2] == container_num[0]:
    ans2 += 1

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
