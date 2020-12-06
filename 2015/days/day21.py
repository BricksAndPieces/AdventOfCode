"""
--- Day 21: RPG Simulator 20XX ---
Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what
equipment to buy at the shop. He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack
reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An
attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score
of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit
point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You
start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats
from all of your items. You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3

You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2
rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy,
for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2
armor:

The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can
spend and still win the fight?

--- Part Two ---
Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules
still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?
"""

from aoc import *

# Change part # to get different part answer
part = 1

weapons = [
    [8, 4, 0],
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0]
]

armors = [
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 4],
    [102, 0, 5],
]

rings = [
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3]
]

inputs = puzzle_input(21, 2015).split('\n')
boss_hp = int(inputs[0].split(' ')[-1])
boss_dmg = int(inputs[1].split(' ')[-1])
boss_armor = int(inputs[2].split(' ')[-1])

shop_combos = []
for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in rings:
                if ring1 != ring2 or True:
                    shop_combos.append([sum(a) for a in zip(weapon, armor, ring1, ring2)])

shop_combos.sort(key=lambda x: x[0], reverse=part == 2)

for combo in shop_combos:
    player_health = 100
    player_dmg = combo[1]
    player_armor = combo[2]
    boss_health = boss_hp

    player_turn = True
    while player_health > 0 and boss_health > 0:
        if player_turn:
            boss_health -= max(1, player_dmg - boss_armor)
        else:
            player_health -= max(1, boss_dmg - player_armor)

        player_turn ^= True

    if player_health > 0 and part == 1:
        print(f'Part 1: {combo[0]}')
        break

    if boss_health > 0 and part == 2:
        print(f'Part 2: {combo[0]}')
        break
