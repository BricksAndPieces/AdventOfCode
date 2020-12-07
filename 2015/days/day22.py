"""
--- Day 22: Wizard Simulator 20XX ---
Little Henry Case decides that defeating bosses with swords and stuff is boring. Now he's playing the game with a
wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes
first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first
character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do magic damage,
your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell,
in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1
damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose.
Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and its
cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it
deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it
gives you 101 new mana.
Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are
created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have,
their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that
would start an effect which is already active. However, effects can be started on the same turn they end.

For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
Now, suppose the same initial conditions, except that the boss has 14 hit points instead:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.

You start with 50 hit points and 500 mana points. The boss's actual stats are in your puzzle input. What is the least
amount of mana you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative
mana.)

--- Part Two ---
On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 1 hit point. If this brings you to or below
0 hit points, you lose.

With the same starting stats for you and the boss, what is the least amount of mana you can spend and still win the
fight?

Inspired by https://github.com/mbb70/adventOfCode/blob/master/d22.py
I was unable to figure out a few bugs in my implementation of the problem
I modified the solution to fit my own implementation (Swapped out the bugs)
"""

import heapq
import math

from aoc import *

# Answer for selected part
part = 1


class GameState:
    def __init__(self, youh, bossh, bossd, ymana, smana, effects):
        self.player_hp = youh
        self.boss_hp = bossh
        self.boss_dmg = bossd
        self.mana = ymana
        self.total_mana = smana
        self.effects = effects

    def trigger_effects(self):
        for effect in self.effects:
            self.effects[effect] -= 1
            if effect == 'poison':
                self.boss_hp -= 3
            elif effect == 'recharge':
                self.mana += 101
        self.effects = { e : v for e,v in self.effects.items() if v > 0 }

    def attack_options(self):
        effects = [e for e, v in self.effects.items() if v > 1]
        return {'missile', 'drain', 'shield', 'poison', 'recharge'}.difference(effects)

    def copy(self):
        return GameState(self.player_hp, self.boss_hp, self.boss_dmg, self.mana, self.total_mana, self.effects.copy())

    def spend_mana(self, m):
        self.mana -= m
        self.total_mana += m

    def player_attack(self, attack):
        if attack == 'shield':
            self.spend_mana(113)
            self.effects[attack] = 6
        elif attack == 'poison':
            self.spend_mana(173)
            self.effects[attack] = 6
        elif attack == 'recharge':
            self.spend_mana(229)
            self.effects[attack] = 5
        elif attack == 'missile':
            self.spend_mana(53)
            self.boss_hp -= 4
        elif attack == 'drain':
            self.spend_mana(73)
            self.boss_hp -= 2
            self.player_hp += 2

    def boss_attack(self):
        self.player_hp -= max(1, self.boss_dmg - (7 if 'shield' in self.effects else 0))

    def children(self):
        children = []
        for attack in self.attack_options():
            s = self.copy()

            if part == 2:
                s.player_hp -= 1
                if s.player_hp == 0:
                    continue

            s.trigger_effects()
            s.player_attack(attack)

            s.trigger_effects()
            if s.boss_hp > 0:
                s.boss_attack()

            if s.player_hp > 0 and s.mana > 0:
                children.append(s)

        return children

    def __lt__(self, other):
        return self.total_mana < other.total_mana

    def __hash__(self):
        return self.__str__().__hash__()

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return "{} {} {} {}".format(self.player_hp, self.boss_hp, self.mana, self.effects)


class PriorityQueue:
    def __init__(self, q):
        self.q = q
        self.in_q = set(q)

    def pop(self, index=0):
        item = self.q.pop(index)
        self.in_q.remove(item)
        return item

    def remove(self, item):
        self.q.remove(item)
        self.in_q.remove(item)

    def add(self, item):
        heapq.heappush(self.q, item)
        self.in_q.add(item)

    def get(self, item):
        return self.q[self.q.index(item)]

    def replace(self, item):
        self.remove(item)
        self.add(item)

    def __bool__(self):
        return len(self.q) != 0

    def __contains__(self, item):
        return item in self.in_q


def dijkstra(node):
    q = PriorityQueue([node])
    visited = set()
    lowest = math.inf
    while q:
        current = q.pop()
        if current.boss_hp <= 0 and current.total_mana < lowest:
            lowest = current.total_mana
        visited.add(current)
        for child in current.children():
            if child.total_mana > lowest:
                continue
            if child not in visited:
                if child not in q:
                    q.add(child)
                elif q.get(child).total_mana > child.total_mana:
                    q.replace(child)
    return lowest


boss_hp, boss_dmg = (int(s.split(':')[1].strip()) for s in puzzle_input(22, 2015).split('\n'))
start = GameState(50, boss_hp, boss_dmg, 500, 0, {})
print(f'Part {part}: {dijkstra(start)}')
