"""
--- Day 7: Amplification Circuit ---
Based on the navigational maps, you're going to need to send more power to your ship's thrusters to reach Santa in time.
To do this, you'll need to configure a series of amplifiers already installed on the ship.

There are five amplifiers connected in series; each one receives an input signal and produces an output signal. They are
connected such that the first amplifier's output leads to the second amplifier's input, the second amplifier's output
leads to the third amplifier's input, and so on. The first amplifier's input value is 0, and the last amplifier's output leads to your ship's thrusters.

    O-------O  O-------O  O-------O  O-------O  O-------O
0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
    O-------O  O-------O  O-------O  O-------O  O-------O
The Elves have sent you some Amplifier Controller Software (your puzzle input), a program that should run on your
existing Intcode computer. Each amplifier will need to run a copy of the program.

When a copy of the program starts running on an amplifier, it will first use an input instruction to ask the amplifier
for its current phase setting (an integer from 0 to 4). Each phase setting is used exactly once, but the Elves can't
remember which amplifier needs which phase setting.

The program will then call another input instruction to get the amplifier's input signal, compute the correct output
signal, and supply it back to the amplifier with an output instruction. (If the amplifier has not yet received an input
signal, it waits until one arrives.)

Your job is to find the largest output signal that can be sent to the thrusters by trying every possible combination of
phase settings on the amplifiers. Make sure that memory is not shared or reused between copies of the program.

For example, suppose you want to try the phase setting sequence 3,1,2,4,0, which would mean setting amplifier A to phase
setting 3, amplifier B to setting 1, C to 2, D to 4, and E to 0. Then, you could determine the output signal that gets
sent from amplifier E to the thrusters with the following steps:

Start the copy of the amplifier controller software that will run on amplifier A. At its first input instruction,
provide it the amplifier's phase setting, 3. At its second input instruction, provide it the input signal, 0. After some
calculations, it will use an output instruction to indicate the amplifier's output signal.
Start the software for amplifier B. Provide it the phase setting (1) and then whatever output signal was produced from
amplifier A. It will then produce a new output signal destined for amplifier C.
Start the software for amplifier C, provide the phase setting (2) and the value from amplifier B, then collect its
output signal.
Run amplifier D's software, provide the phase setting (4) and input value, and collect its output signal.
Run amplifier E's software, provide the phase setting (0) and input value, and collect its output signal.
The final output signal from amplifier E would be sent to the thrusters. However, this phase setting sequence may not
have been the best one; another sequence might have sent a higher signal to the thrusters.

Here are some example programs:

Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):

3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):

3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0
Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):

3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
Try every combination of phase settings on the amplifiers. What is the highest signal that can be sent to the thrusters?

--- Part Two ---
It's no good - in this configuration, the amplifiers can't generate a large enough output signal to produce the thrust
you'll need. The Elves quickly talk you through rewiring the amplifiers into a feedback loop:

      O-------O  O-------O  O-------O  O-------O  O-------O
0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-.
   |  O-------O  O-------O  O-------O  O-------O  O-------O |
   |                                                        |
   '--------------------------------------------------------+
                                                            |
                                                            v
                                                     (to thrusters)
Most of the amplifiers are connected as they were before; amplifier A's output is connected to amplifier B's input, and
so on. However, the output from amplifier E is now connected into amplifier A's input. This creates the feedback loop:
the signal will be sent through the amplifiers many times.

In feedback loop mode, the amplifiers need totally different phase settings: integers from 5 to 9, again each used
exactly once. These settings will cause the Amplifier Controller Software to repeatedly take input and produce output
many times before halting. Provide each amplifier its phase setting at its first input instruction; all further
input/output instructions are for signals.

Don't restart the Amplifier Controller Software on any amplifier during this process. Each one should continue receiving
and sending signals until it halts.

All signals sent or received in this process will be between pairs of amplifiers except the very first signal and the
very last signal. To start the process, a 0 signal is sent to amplifier A's input exactly once.

Eventually, the software on the amplifiers will halt after they have processed the final loop. When this happens, the
last output signal from amplifier E is sent to the thrusters. Your job is to find the largest output signal that can be
sent to the thrusters using the new phase settings and feedback loop arrangement.

Here are some example programs:

Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):

3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):

3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
Try every combination of the new phase settings on the amplifier feedback loop. What is the highest signal that can be
sent to the thrusters?
"""

from aoc import *
from itertools import permutations


class Computer:
    def __init__(self, program, phase):
        self.program = program
        self.phase = phase
        self.phase_inputted = False
        self.index = 0
        self.halted = False

    def get_args(self):
        instruction = f'{self.program[self.index]:05}'
        op = int(instruction[3:])
        params = [int(s) for s in instruction[:3]]

        mode_a, mode_b, mode_c = params
        args = []
        if op in [1, 2, 4, 5, 6, 7, 8]:
            if mode_c == 0:
                args.append(self.program[self.program[self.index + 1]])
            else:
                args.append(self.program[self.index + 1])

            if op in [1, 2, 5, 6, 7, 8]:
                if mode_b == 0:
                    args.append(self.program[self.program[self.index + 2]])
                else:
                    args.append(self.program[self.index + 2])

                if op in []:
                    if mode_a == 0:
                        args.append(self.program[self.program[self.index + 3]])
                    else:
                        args.append(self.program[self.index + 3])

        return op, args

    def output(self, code_input):
        while self.program[self.index] != 99:
            op, args = self.get_args()
            if op == 1:
                self.program[self.program[self.index + 3]] = args[0] + args[1]
                self.index += 4
            elif op == 2:
                self.program[self.program[self.index + 3]] = args[0] * args[1]
                self.index += 4
            elif op == 3:
                self.program[self.program[self.index + 1]] = code_input if self.phase_inputted else self.phase
                self.phase_inputted = True
                self.index += 2
            elif op == 4:
                self.index += 2
                return args[0]
            elif op == 5:
                self.index = args[1] if args[0] else self.index + 3
            elif op == 6:
                self.index = args[1] if not args[0] else self.index + 3
            elif op == 7:
                self.program[self.program[self.index + 3]] = 1 if args[0] < args[1] else 0
                self.index += 4
            elif op == 8:
                self.program[self.program[self.index + 3]] = 1 if args[0] == args[1] else 0
                self.index += 4
            else:
                print(self.program)
                raise Exception(f'Invalid Opcode: {op}')

        self.halted = True


def part1(inputs):
    max_thrust = 0
    phases = permutations([0, 1, 2, 3, 4])
    for phase in phases:
        code_input = 0

        for i in phase:
            program = inputs.copy()
            comp = Computer(program, i)
            code_input = comp.output(code_input)

        max_thrust = max(max_thrust, code_input)

    return max_thrust


def part2(inputs):
    max_thrust = 0
    phases = permutations([5, 6, 7, 8, 9])
    for phase in phases:
        code_input = 0
        comps = [Computer(inputs.copy(), i) for i in phase]

        while not comps[0].halted:
            for comp in comps:
                val = comp.output(code_input)
                if val is not None:
                    code_input = val

        max_thrust = max(max_thrust, code_input)

    return max_thrust


puzzle_input = ints(puzzle_input(7, 2019), ',')
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
