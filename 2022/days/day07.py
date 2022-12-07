"""
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7
"""

from collections import defaultdict
from aoc import *

inputs = puzzle_input(7, 2022, sample=False).split('$ ')[1:]

file_system = defaultdict(lambda: [])
cur_path = ''

for line in inputs:
    if line.startswith('cd'):
        arg = line[3:-1]
        if arg == '/':
            cur_path = ''
        elif arg == '..':
            cur_path = '/'.join(cur_path.split('/')[:-1])
        else:
            cur_path += '/' + arg
        
    if line.startswith('ls'):
        for elem in line.rstrip().split('\n')[1:]:
            size, name = elem.split(' ')
            file_system[cur_path].append(name if size == 'dir' else int(size))

def folder_size(file_path):
    size = lambda f: f if type(f) is int else folder_size(file_path + '/' + f)
    return sum(size(f) for f in file_system[file_path])

folder_sizes = [folder_size(f) for f in file_system]
ans = sum(f for f in folder_sizes if f < 100000)
print(f'Part 1: {ans}')

needed_space = folder_size('') - 40000000
delete_file = next(f for f in sorted(folder_sizes) if f > needed_space)
print(f'Part 2: {delete_file}')
