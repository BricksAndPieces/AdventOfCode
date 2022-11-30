"""
Problem here
"""

from aoc import *
from hashlib import md5

door_id = puzzle_input(5, 2016)

# index = 0
# password = ''
# while len(password) < 8:
#     hashing = f'{door_id}{index}'
#     hashcode = md5(bytes(hashing, encoding='utf-8')).hexdigest()
#     if hashcode.startswith('0' * 5):
#         password = f'{password}{hashcode[5]}'
#
#     index += 1
#
# print(f'Part 1: {password}')

index = 0
password = ['' for _ in [*range(8)]]
while '' in password:
    hashing = f'{door_id}{index}'
    hashcode = md5(bytes(hashing, encoding='utf-8')).hexdigest()
    if hashcode.startswith('0' * 5):
        pos = hashcode[5]
        char = hashcode[6]

        if pos in '01234567':
            password[int(pos)] = char
            print(char)

    index += 1

password = ''.join(password)
print(f'Part 2: {password}')
