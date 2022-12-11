"""
--- Day 11: Monkey in the Middle ---
https://adventofcode.com/2022/day/11
"""

from dataclasses import dataclass
from aoc import *

@dataclass
class Monkey:
    items: list
    operation: tuple[str, str, str]
    test: tuple[int, int, int]
    n_inspect: int = 0

    def op(self, var, worry):
        return worry if var == 'old' else int(var)

    def inspect(self, prime_reducer, part1):
        self.n_inspect += 1

        item = self.items[0]
        del self.items[0]

        a = self.op(self.operation[0], item)
        b = self.op(self.operation[2], item)
        worry = a * b if self.operation[1] == '*' else a + b

        if part1:
            worry //= 3

        worry %= prime_reducer
        return worry, self.test[1] if worry % self.test[0] == 0 else self.test[2]

        
inputs = puzzle_input(11, 2022, sample=False).split('\n\n')

def monkey_biz(rounds, part1):
    monkeys = []
    for raw_monkey in inputs:
        lines = raw_monkey.split('\n')
        items = ints(lines[1][18:], ',')
        operation = tuple(lines[2][19:].split(' '))
        test = tuple(int(lines[i].split(' ')[-1]) for i in range(3, 6))
        monkeys.append(Monkey(items, operation, test))

    prime_reducer = mult(set(m.test[0] for m in monkeys))

    for _ in range(rounds):
        for m in monkeys:
            while m.items:
                worry, reciever = m.inspect(prime_reducer, part1)
                monkeys[reciever].items.append(worry)
    
    return mult(m.n_inspect for m in sorted(monkeys, key=lambda x: x.n_inspect)[-2:])

print(f'Part 1: {monkey_biz(20, True)}')
print(f'Part 2: {monkey_biz(10000, False)}')
