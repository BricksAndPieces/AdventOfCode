"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a
little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal
is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one
source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a
signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and
y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the
circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these
gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided
to wire a?

--- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a).
What new signal is ultimately provided to wire a?
"""

from aoc import *


def get_wire(inputs, wires, key):
    if key.isdigit():
        return int(key)

    if key in wires:
        return wires[key]

    for i in inputs:
        parts = i.split(' ')
        if parts[-1] == key:
            if 'AND' in i:
                wires[key] = get_wire(inputs, wires, parts[0]) & get_wire(inputs, wires, parts[2])
                return wires[key]
            elif 'OR' in i:
                wires[key] = get_wire(inputs, wires, parts[0]) | get_wire(inputs, wires, parts[2])
                return wires[key]
            elif 'LSHIFT' in i:
                wires[key] = get_wire(inputs, wires, parts[0]) << get_wire(inputs, wires, parts[2])
                return wires[key]
            elif 'RSHIFT' in i:
                wires[key] = get_wire(inputs, wires, parts[0]) >> get_wire(inputs, wires, parts[2])
                return wires[key]
            elif 'NOT' in i:
                wires[key] = ~ get_wire(inputs, wires, parts[1])
                return wires[key]
            else:
                wires[key] = get_wire(inputs, wires, parts[0])
                return wires[key]


def part1(inputs):
    return get_wire(inputs, {}, 'a')


def part2(inputs):
    return get_wire(inputs, {'b': 956}, 'a')


puzzle_input = puzzle_input(7, 2015).split('\n')
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
