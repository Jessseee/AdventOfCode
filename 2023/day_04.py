# Day 4 of Advent of Code 2023
# Scratchcards

# The gondola ride brings us to a new sky-island named Island Island
# (because it is a floating island with islands). Here we meet another Elf
# who runs the Gondola station. They apparently received a bunch of scratchcards
# as a gift, but have no idea how to find out what they won. Our task is to find
# out how to score the scratchcards, so the Elf can go collect their price.

from aoc.helpers import *


def parse_card(card):
    numbers = card.split(":")[1].split("|")
    return [tuple(int(n) for n in re.findall(r"\d+", l)) for l in numbers]


def count_cards(key, card_dict, acc=1):
    for other_key in card_dict[key]:
        acc += count_cards(other_key, card_dict)
    return acc


if __name__ == "__main__":
    score, cards = 0, {}
    for i, (numbers, winning) in enumerate(import_input("\n", parse_card), start=1):
        matches = [number for number in numbers if number in winning]
        score += 2 ** (len(matches) - 1) if len(matches) > 0 else 0
        cards[i] = list(range(i + 1, i + 1 + len(matches)))

    total_nr_cards = 0
    for key in cards.keys():
        total_nr_cards += count_cards(key, cards)

    print("The total scratchcard score:", c(score, Color.GREEN))
    print("The number of recursively counted cards:", c(total_nr_cards, Color.GREEN))
