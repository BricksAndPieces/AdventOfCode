"""
--- Day 3: Squares With Three Sides ---
Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this
part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't
triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given
above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

--- Part Two ---
Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of
three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
"""

from aoc import *
import re


def part1(inputs):
    num_regex = re.compile('\\d+')
    count = 0
    for i in inputs:
        nums = num_regex.findall(i)
        nums = sorted([int(s) for s in nums])
        if nums[0] + nums[1] > nums[2]:
            count += 1

    return count


def part2(inputs):
    num_regex = re.compile('\\d+')
    count = 0

    for i in range(0, len(inputs), 3):
        cols = []
        for j in range(3):
            nums = num_regex.findall(inputs[i+j])
            nums = [int(s) for s in nums]
            cols.append(nums)

        for j in range(3):
            row = sorted([cols[0][j], cols[1][j], cols[2][j]])
            if row[0] + row[1] > row[2]:
                count += 1

    return count


puzzle_input = puzzle_input(3, 2016).split('\n')
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
