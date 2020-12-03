"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of
the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules
overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or
nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or
aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even
aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter
between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the
letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
"""

from aoc import *


def three_vowels(phrase):
    v = ['a', 'e', 'i', 'o', 'u']
    c = 0
    for s in phrase:
        if s in v:
            c += 1

    return c >= 3


def double_letter(phrase):
    for i in range(len(phrase) - 1):
        if phrase[i] == phrase[i + 1]:
            return True


def has_illegal(phrase):
    x = ['ab', 'cd', 'pq', 'xy']
    for z in x:
        if z in phrase:
            return True


def letter_pair(phrase):
    for i in range(len(phrase)-1):
        z = phrase[i:i+2]
        x = phrase.replace(z, '')
        if len(phrase) - len(x) >= 4:
            return True


def repeating_letter(phrase):
    for i in range(len(phrase)-2):
        if phrase[i] == phrase[i+2]:
            return True


def part1(inputs):
    count = 0
    for i in inputs:
        if three_vowels(i) and double_letter(i) and not has_illegal(i):
            count += 1

    return count


def part2(inputs):
    count = 0
    for i in inputs:
        if letter_pair(i) and repeating_letter(i):
            count += 1

    return count


puzzle_input = puzzle_input(5, 2015).split('\n')
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
