"""
--- Day 13: Care Package ---
As you ponder the solitude of space and the ever-increasing three-hour roundtrip for messages between you and Earth,
you notice that the Space Mail Indicator Light is blinking. To help keep you sane, the Elves have sent you a care
package.

It's a new game for the ship's arcade cabinet! Unfortunately, the arcade is all the way on the other end of the ship.
Surely, it won't be hard to build your own - the care package even comes with schematics.

The arcade cabinet runs Intcode software like the game the Elves sent (your puzzle input). It has a primitive screen
capable of drawing square tiles on a grid. The software draws tiles to the screen with output instructions: every three
output instructions specify the x position (distance from the left), y position (distance from the top), and tile id.
The tile id is interpreted as follows:

0 is an empty tile. No game object appears in this tile.
1 is a wall tile. Walls are indestructible barriers.
2 is a block tile. Blocks can be broken by the ball.
3 is a horizontal paddle tile. The paddle is indestructible.
4 is a ball tile. The ball moves diagonally and bounces off objects.
For example, a sequence of output values like 1,2,3,6,5,4 would draw a horizontal paddle tile (1 tile from the left and
2 tiles from the top) and a ball tile (6 tiles from the left and 5 tiles from the top).

Start the game. How many block tiles are on the screen when the game exits?

--- Part Two ---
The game didn't run because you didn't put in any quarters. Unfortunately, you did not bring any quarters. Memory
address 0 represents the number of quarters that have been inserted; set it to 2 to play for free.

The arcade cabinet has a joystick that can move left and right. The software reads the position of the joystick with
input instructions:

If the joystick is in the neutral position, provide 0.
If the joystick is tilted to the left, provide -1.
If the joystick is tilted to the right, provide 1.
The arcade cabinet also has a segment display capable of showing a single number that represents the player's current
score. When three output instructions specify X=-1, Y=0, the third output instruction is not a tile; the value instead
specifies the new score to show in the segment display. For example, a sequence of output values like -1,0,12345 would
show 12345 as the player's current score.

Beat the game by breaking all the blocks. What is your score after the last block is broken?
"""

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


inputs = ints(puzzle_input(13, 2019), ',')
comp = Computer(inputs)

count = 0
while not comp.halted:
    for _ in range(3):
        result = comp.output('')

    if result == 2:
        count += 1

print(f'Part 1: {count}')


def joystick(ball, paddle):
    if ball > paddle:
        return 1
    if paddle > ball:
        return -1

    return 0


inputs[0] = 2
comp = Computer(inputs)
ball = paddle = 0
pos = {}

while not comp.halted:
    for output in range(3):
        pos[output] = comp.output(joystick(ball, paddle))

    if pos[2] == 3:
        paddle = pos[0]
    elif pos[2] == 4:
        ball = pos[0]

    if pos[0] == -1:
        score = pos[2]


print(f'Part 2: {score}')
