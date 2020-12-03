"""
--- Day 11: Corporate Policy ---
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password
based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for
security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step;
if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They
cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement
(because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).

The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi...,
since i is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?

--- Part Two ---
Santa's password expired again. What's the next one?
"""

from aoc import *

alphabet = 'abcdefghijklmnopqrstuvwxyz'
two_pairs = [x * 2 for x in alphabet]
three_pairs = [alphabet[x:x + 3] for x in range(24)]


def two_pair(password):
    count = 0
    for x in two_pairs:
        if x in password:
            count += 1

    return count >= 2


def three_pair(password):
    for x in three_pairs:
        if x in password:
            return True


def has_illegal_chars(password):
    for c in ['i', 'o', 'l']:
        if c in password:
            return True


def increment_char(c):
    return chr(ord(c) + 1) if c != 'z' else 'a'


def increment_password(password):
    digit = -1
    password = list(password)
    password[digit] = increment_char(password[digit])
    while password[digit] == 'a':
        digit -= 1
        password[digit] = increment_char(password[digit])

    return ''.join(password)


def part1(inputs):
    password = increment_password(inputs)
    while not (two_pair(password) and three_pair(password) and not has_illegal_chars(password)):
        password = increment_password(password)

    return password


def part2(inputs):
    password = increment_password(part1(inputs))
    while not (two_pair(password) and three_pair(password) and not has_illegal_chars(password)):
        password = increment_password(password)

    return password


puzzle_input = puzzle_input(11, 2015)
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
