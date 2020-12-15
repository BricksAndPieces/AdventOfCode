"""
--- Day 11: Space Police ---
On the way to Jupiter, you're pulled over by the Space Police.

"Attention, unmarked spacecraft! You are in violation of Space Law! All spacecraft must have a clearly visible
registration identifier! You have 24 hours to comply or be sent to Space Jail!"

Not wanting to be sent to Space Jail, you radio back to the Elves on Earth for help. Although it takes almost three
hours for their reply signal to reach you, they send instructions for how to power up the emergency hull painting robot
and even provide a small Intcode program (your puzzle input) that will cause it to paint your ship appropriately.

There's just one problem: you don't have an emergency hull painting robot.

You'll need to build a new emergency hull painting robot. The robot needs to be able to move around on the grid of
square panels on the side of your ship, detect the color of its current panel, and paint its current panel black or
white. (All of the panels are currently black.)

The Intcode program will serve as the brain of the robot. The program uses input instructions to access the robot's
camera: provide 0 if the robot is over a black panel or 1 if the robot is over a white panel. Then, the program will
output two values:

First, it will output a value indicating the color to paint the panel the robot is over: 0 means to paint the panel
black, and 1 means to paint the panel white.
Second, it will output a value indicating the direction the robot should turn: 0 means it should turn left 90 degrees,
and 1 means it should turn right 90 degrees.
After the robot turns, it should always move forward exactly one panel. The robot starts facing up.

The robot will continue running for a while like this and halt when it is finished drawing. Do not restart the Intcode
computer inside the robot during this process.

For example, suppose the robot is about to start running. Drawing black panels as ., white panels as #, and the robot
pointing the direction it is facing (< ^ > v), the initial state and region near the robot looks like this:

.....
.....
..^..
.....
.....
The panel under the robot (not visible here because a ^ is shown instead) is also black, and so any input instructions
at this point should be provided 0. Suppose the robot eventually outputs 1 (paint white) and then 0 (turn left). After
taking these actions and moving forward one panel, the region now looks like this:

.....
.....
.<#..
.....
.....
Input instructions should still be provided 0. Next, the robot might output 0 (paint black) and then 0 (turn left):

.....
.....
..#..
.v...
.....
After more outputs (1,0, 1,0):

.....
.....
..^..
.##..
.....
The robot is now back where it started, but because it is now on a white panel, input instructions should be provided 1.
After several more outputs (0,1, 1,0, 1,0), the area looks like this:

.....
..<#.
...#.
.##..
.....
Before you deploy the robot, you should probably have an estimate of the area it will cover: specifically, you need to
know the number of panels it paints at least once, regardless of color. In the example above, the robot painted 6 panels
at least once. (It painted its starting panel twice, but that panel is still only counted once; it also never painted
the panel it ended on.)

Build a new emergency hull painting robot and run the Intcode program on it. How many panels does it paint at least
once?

--- Part Two ---
You're not sure what it's trying to paint, but it's definitely not a registration identifier. The Space Police are
getting impatient.

Checking your external ship cameras again, you notice a white panel marked "emergency hull painting robot starting
panel". The rest of the panels are still black, but it looks like the robot was expecting to start on a white panel, not
a black one.

Based on the Space Law Space Brochure that the Space Police attached to one of your windows, a valid registration
identifier is always eight capital letters. After starting the robot on a single white panel instead, what registration
identifier does it paint on your hull?
"""

from collections import defaultdict
from aoc import *


class Computer:

    def __init__(self, program):
        from collections import defaultdict
        self.program = defaultdict(lambda: 0)
        for i, n in enumerate(program):
            self.program[i] = n

        self.index = 0
        self.halted = False
        self.relative_base = 0

    def get_args(self):
        # Parameter Modes:
        # 0 - Position Mode
        # 1 - Immediate Mode
        # 2 - Relative Mode

        instruction = f'{self.program[self.index]:05}'
        op = int(instruction[3:])
        params = [int(s) for s in instruction[:3]]

        mode_a, mode_b, mode_c = params
        args = []

        if op in [1, 2, 4, 5, 6, 7, 8, 9]:
            if mode_c == 0:
                args.append(self.program[self.program[self.index + 1]])
            elif mode_c == 1:
                args.append(self.program[self.index + 1])
            elif mode_c == 2:
                args.append(self.program[self.relative_base + self.program[self.index + 1]])

        if op in [1, 2, 5, 6, 7, 8]:
            if mode_b == 0:
                args.append(self.program[self.program[self.index + 2]])
            elif mode_b == 1:
                args.append(self.program[self.index + 2])
            elif mode_b == 2:
                args.append(self.program[self.relative_base + self.program[self.index + 2]])

        if op in []:
            if mode_a == 0:
                args.append(self.program[self.program[self.index + 3]])
            elif mode_a == 1:
                args.append(self.program[self.index + 3])
            elif mode_a == 2:
                args.append(self.program[self.relative_base + self.program[self.index + 3]])

        offset = 0
        if op in [1, 2, 7, 8] and mode_a == 2:
            offset = self.relative_base

        if op in [3] and mode_c:
            offset = self.relative_base

        return op, args, offset

    def output(self, code_input):
        while self.program[self.index] != 99:
            op, args, offset = self.get_args()
            if op == 1:
                self.program[self.program[self.index + 3] + offset] = args[0] + args[1]
                self.index += 4
            elif op == 2:
                self.program[self.program[self.index + 3] + offset] = args[0] * args[1]
                self.index += 4
            elif op == 3:
                self.program[self.program[self.index + 1] + offset] = code_input
                self.index += 2
            elif op == 4:
                self.index += 2
                return args[0]
            elif op == 5:
                self.index = args[1] if args[0] else self.index + 3
            elif op == 6:
                self.index = args[1] if not args[0] else self.index + 3
            elif op == 7:
                self.program[self.program[self.index + 3] + offset] = 1 if args[0] < args[1] else 0
                self.index += 4
            elif op == 8:
                self.program[self.program[self.index + 3] + offset] = 1 if args[0] == args[1] else 0
                self.index += 4
            elif op == 9:
                self.relative_base += args[0]
                self.index += 2
            else:
                print(self.program)
                raise Exception(f'Invalid Opcode: {op}')

        self.halted = True


def solve(part1=True):
    inputs = ints(puzzle_input(11, 2019), ',')
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    facing = 0

    painted = set()
    panels = defaultdict(int)
    current = (0, 0)
    panels[current] = 0 if part1 else 1
    comp = Computer(inputs)

    while not comp.halted:
        painted.add(current)
        output = comp.output(panels[current])
        panels[current] = output
        direction = comp.output(panels[current])

        if direction == 0:
            facing -= 1
        elif direction == 1:
            facing += 1

        facing %= 4
        move = dirs[facing]
        current = (current[0] + move[0], current[1] + move[1])

    return painted, panels


part1 = solve()
print(f'Part 1: {len(part1[0])}')

print('Part 2:')
_, panels = solve(False)
for x in reversed(range(0, 45)):
    s = []
    for y in reversed(range(-30, 15)):
        s.append('@' if panels[x, y] else ' ')

    print(' '.join(s))
