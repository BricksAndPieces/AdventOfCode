"""
--- Day 16: Packet Decoder ---
https://adventofcode.com/2021/day/16
"""

from aoc import *

inputs = puzzle_input(16, 2021, sample=False)
inputs = '{0:08b}'.format(int(inputs, 16))
inputs = ('0' * (4 - a) + inputs) if (a := len(inputs) % 4) else inputs

version_numbers = []
type_map = {
    0: sum,
    1: mult,
    2: min,
    3: max,
    5: lambda a: int(a[0] > a[1]),
    6: lambda a: int(a[0] < a[1]),
    7: lambda a: int(a[0] == a[1]),
}


def literal_value(packet):
    value = ''
    while packet[0] == '1':
        value += packet[1:5]
        packet = packet[5:]

    value += packet[1:5]
    return int(value, 2), packet[5:]


def parse(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3: 6], 2)
    packet = packet[6:]

    value = 0
    version_numbers.append(version)

    if type_id == 4:  # Literal Value
        value, packet = literal_value(packet)
    elif type_id != 4:  # Operator
        length_id, packet = packet[0], packet[1:]
        values = []

        if length_id == '0':
            length_bits, packet = int(packet[:15], 2), packet[15:]
            sub_packet, packet = packet[:length_bits], packet[length_bits:]
            while sub_packet:
                v, sub_packet = parse(sub_packet)
                values.append(v)

        elif length_id == '1':
            num_subs, packet = int(packet[:11], 2), packet[11:]
            for _ in range(0, num_subs):
                v, packet = parse(packet)
                values.append(v)

        value = type_map[type_id](values)

    return value, packet


part2 = parse(inputs)[0]
print(f'Part 1: {sum(version_numbers)}')
print(f'Part 2: {part2}')
