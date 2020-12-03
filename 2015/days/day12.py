"""
--- Day 12: JSAbacusFramework.io ---
Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software
uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and
strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

--- Part Two ---
Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects
({...}), not arrays ([...]).

[1,2,3] still has a sum of 6.
[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.


DISCLAIMER:
Inspiration for part 2 taken from https://github.com/snowbagoly/adventofcode2015/blob/master/day12.py
I couldn't figure out how to correctly traverse the json object.

TODO
Come back and create my own implementation of the solution.
"""

from aoc import *
import re


def part1(inputs):
    nums = re.findall('-?\\d+', inputs)
    return sum([int(s) for s in nums])


def part2(inputs):
    number_regex = re.compile('-?\\d+')
    q = [eval(inputs)]
    no_red_summa = 0
    while q:
        p = q.pop(0)
        if isinstance(p, list):
            for val in p:
                if number_regex.match(str(val)):
                    no_red_summa += val
                elif isinstance(val, list) or isinstance(val, dict):
                    q.append(val)

        else:
            has_red_key = any(p[key] == "red" for key in p)
            if not has_red_key:
                for key in p:
                    if number_regex.match(str(p[key])):
                        no_red_summa += p[key]
                    elif isinstance(p[key], list) or isinstance(p[key], dict):
                        q.append(p[key])

    return no_red_summa


puzzle_input = puzzle_input(12, 2015)
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
