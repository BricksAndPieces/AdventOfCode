"""
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3
"""

from aoc import *

inputs = puzzle_input(3, 2023, sample=False).split('\n')
inputs = ['.' * (len(inputs[0])+2)] + ['.' + line + '.' for line in inputs] + ['.' * (len(inputs[0])+2)]

#  --- part 1 --- 

ans = 0
for x in range(1, len(inputs)):
    num = ''
    for y in range(1, len(inputs[0])):
        if inputs[x][y].isdigit():
            num += inputs[x][y]
            continue

        if num == '':
            continue

        bad = ('.' * (len(num)+3)) + num + ('.' * (len(num)+3))
        real = ''.join(inputs[x-i][y-len(num)-1:y+1] for i in (1, 0, -1))

        if bad != real:
            ans += int(num)

        num = ''
        
print(f'Part 1: {ans}')

#  --- part 2 --- 

ans = 0
for x in range(len(inputs)):
    for y in range(len(inputs[0])):
        if inputs[x][y] != '*':
            continue

        vals = []

        for k in (1, 0, -1):
            if inputs[x+k][y].isdigit():
                num = inputs[x+k][y]
                for i in range(y+1, len(inputs)):
                    if inputs[x+k][i].isdigit():
                        num += inputs[x+k][i]
                    else:
                        break
                for i in range(y-1, -1, -1):
                    if inputs[x+k][i].isdigit():
                        num = inputs[x+k][i] + num
                    else:
                        break
                if num:
                    vals.append(int(num))

            else:
                if inputs[x+k][y+1].isdigit():
                    num = ''
                    for i in range(y+1, len(inputs)):
                        if inputs[x+k][i].isdigit():
                            num += inputs[x+k][i]
                        else:
                            break
                        
                    if num:
                        vals.append(int(num))
            
                if inputs[x+k][y-1].isdigit():
                    num = ''
                    for i in range(y-1, -1, -1):
                        if inputs[x+k][i].isdigit():
                            num = inputs[x+k][i] + num
                        else:
                            break
                    if num:
                        vals.append(int(num))

        if len(vals) == 2:
            ans += vals[0] * vals[1]

print(f'Part 2: {ans}')
