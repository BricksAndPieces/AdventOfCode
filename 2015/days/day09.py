"""
--- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of
locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once.
What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?\

--- Part Two ---
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly
once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""

from aoc import *
from itertools import permutations


def part1(inputs):
    least = 70374983748973289472397
    c = ['Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight']
    for z in permutations(c):
        count = 0
        for v in range(len(z)-1):
            count += inputs[z[v], z[v+1]]

        least = min(count, least)

    return least


def part2(inputs):
    most = 0
    c = ['Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight']
    for z in permutations(c):
        count = 0
        for v in range(len(z) - 1):
            count += inputs[z[v], z[v + 1]]

        most = max(count, most)

    return most


puzzle_routes = {}
for i in puzzle_input(9, 2015).split('\n'):
    parts = i.split(' ')
    puzzle_routes[parts[0], parts[2]] = int(parts[-1])
    puzzle_routes[parts[2], parts[0]] = int(parts[-1])

print(f'Part 1: {part1(puzzle_routes)}')
print(f'Part 2: {part2(puzzle_routes)}')
