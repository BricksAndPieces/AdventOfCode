"""
--- Day 21: Allergen Assessment ---
You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't
even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your
journey.

You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in
a language you do understand. You should be able to use this information to determine which ingredient contains which
allergen and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's
ingredients list followed by some or all of the allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always
marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains
each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed,
the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was
labeled in a language you don't know.

For example, consider the following list of foods:

mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and
nhms. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward:
dairy and fish.

The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list.
In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the number of
times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which
appears twice.

Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those
ingredients appear?

--- Part Two ---
Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient
contains which allergen.

In the above example:

mxmxvkd contains dairy.
sqjhc contains fish.
fvjkl contains soy.
Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous
ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example,
this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous ingredient list?
"""

from aoc import *
import re

inputs = puzzle_input(21, 2020, sample=False).split('\n')

foods = []
all_allergens = set()
all_ingredients = set()

for line in inputs:
    ingredients = line[:line.index('(')-1].split(' ')
    allergens = [a.strip() for a in line[line.index('contains ')+9:-1].split(',')]
    foods.append((ingredients, allergens))
    all_allergens |= set(allergens)
    all_ingredients |= set(ingredients)

bad_ingredients = dict()
all_bad_ingredients = set()
for allergen in all_allergens:
    bad = set(all_ingredients)
    for food in [f for f in foods if allergen in f[1]]:
        bad = bad.intersection(food[0])

    bad_ingredients[allergen] = list(bad)
    all_bad_ingredients |= bad

total = sum(len(x[0]) for x in foods)
num_bad = sum(sum(x[0].count(bad) for x in foods) for bad in all_bad_ingredients)
print(f'Part 1: {total - num_bad}')

dangerous = {}
while len(dangerous) < len(all_allergens):
    for a, i in bad_ingredients.items():
        if len(i) == 1:
            ingredient = i[0]
            dangerous[ingredient] = a

            for key in bad_ingredients:
                if ingredient in bad_ingredients[key]:
                    bad_ingredients[key].remove(ingredient)

dangerous_list = sorted(dangerous.keys(), key=lambda x: dangerous[x])
dangerous_list = re.sub(r'\'|\[|\]| ', '', str(dangerous_list))
print(f'Part 2: {dangerous_list}')
