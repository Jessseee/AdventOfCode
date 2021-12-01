# Day 21 Advent of Code
# I might be allergic to that
from helpers import *
import re

if __name__ == '__main__':
    menu = import_input().read().split('\n')
    allergens_dict = {}
    no_allergens = set()
    foods = {tuple(ingredients.split(' ')): allergens.split(', ') for ingredients, allergens in [re.search(r'(.*) \(contains (.*)\)$', food).groups() for food in menu]}

    for ingredients, allergens in foods.items():
        for allergen in allergens:
            if allergen in allergens_dict:
                allergens_dict[allergen] = allergens_dict.get(allergen).intersection(ingredients)
            else:
                allergens_dict[allergen] = set(ingredients)

    count = 0
    for ingredients in foods:
        for ingredient in ingredients:
            if ingredient not in sorted({x for v in allergens_dict.values() for x in v}):
                no_allergens.add(ingredient)
                count += 1
    print(count)

    taken = []
    for key in sorted(allergens_dict, key=lambda key: len(allergens_dict[key])):
        print(key, allergens_dict[key])
        for ingredient in taken:
            if ingredient in allergens_dict[key]:
                allergens_dict[key].remove(ingredient)
        for ingredient in allergens_dict[key]:
            taken.append(ingredient)
        print(key, allergens_dict[key])
    print(sorted(list(allergens_dict.keys())))
    print(allergens_dict)
    print(no_allergens)

