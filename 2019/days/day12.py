"""
Problem here
"""

from itertools import combinations, permutations, product
from functools import lru_cache
import numpy as np
import re

from aoc import *
from math import gcd
from functools import reduce


class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]

    def update_position(self):
        self.position = tuple(map(sum, zip(self.position, self.velocity)))

    def update_velocity(self, others):
        for moon in others:
            if moon is self:
                continue

            for i in range(3):
                if self.position[i] > moon.position[i]:
                    self.velocity[i] -= 1
                elif self.position[i] < moon.position[i]:
                    self.velocity[i] += 1

    def potential_energy(self):
        return sum(abs(x) for x in self.position)

    def kinetic_energy(self):
        return sum(abs(x) for x in self.velocity)

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def state(self):
        return self.position + tuple(self.velocity)


def state_of_moons(moons):
    state = tuple()
    for moon in moons:
        state += moon.state()

    return state


inputs = puzzle_input(12, 2019).split('\n')
moons = []
for line in inputs:
    parts = line.replace('<', '').replace('>', '').replace(' ', '').split(',')
    moons.append(Moon(tuple([int(part[2:]) for part in parts])))

for _ in range(1000):
    [moon.update_velocity(moons) for moon in moons]
    [moon.update_position() for moon in moons]


total_energy = sum(moon.total_energy() for moon in moons)
print(f'Part 1: {total_energy}')

moons = []
for line in inputs:
    parts = line.replace('<', '').replace('>', '').replace(' ', '').split(',')
    moons.append(Moon(tuple([int(part[2:]) for part in parts])))

steps = [0, 0, 0]
for dim in range(3):
    moons_dim = [moon.position[dim] for moon in moons]
    velocities_dim = [moon.velocity[dim] for moon in moons]
    start_state = tuple(moons_dim + velocities_dim)

    while True:
        for m1 in range(3):
            for m2 in range(m1 + 1, 4):
                if moons_dim[m1] > moons_dim[m2]:
                    velocities_dim[m1] -= 1
                    velocities_dim[m2] += 1
                elif moons_dim[m1] < moons_dim[m2]:
                    velocities_dim[m1] += 1
                    velocities_dim[m2] -= 1

        moons_dim = [moons_dim[i] + velocities_dim[i] for i in range(4)]
        steps[dim] += 1

        if start_state == tuple(moons_dim + velocities_dim):
            break

t = reduce(lambda a, b: a * b // gcd(a, b), steps)
print(f'Part 2: {t}')
