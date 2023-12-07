# Day 7 of Advent of Code 2023
# Camel Cards

# We take the short airship flight to Desert Island where we find an Elf completely covered in white clothing,
# wearing goggles and riding a large camel. They ask us whether we have brought the parts to fix the water
# filtering machine. Of course, we have not brought "the parts", however we can help them figure out why they
# stopped receiving the parts for the machine. It will take a while to get there though, so in the meanwhile
# we play a few games of Camel Cards. It is sort of similar to poker, but easier to play on a camels back.
# Of course, we will be bidding on the games. Our task is to find out what our winnings will be. We find our
# winnings by sorting our hands of cards by strength and summing the bids on those hands.

from collections import Counter

from aoc.helpers import *


class Hand:
    card_map = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def __init__(self, cards, bid, use_jokers=False):
        self.use_jokers = use_jokers
        self.type = self._type(cards)
        self.cards = self._cards(cards)
        self.bid = int(bid)

    def _cards(self, cards):
        return [self._card(card) for card in cards]

    def _card(self, card):
        return 0 if card == "J" and self.use_jokers else self.card_map.index(card)

    def _type(self, cards):
        most_common, second_most_common = self._count(cards)
        if most_common == 5:
            return 6
        elif most_common == 4:
            return 5
        elif most_common + second_most_common == 5:
            return 4
        elif most_common == 3:
            return 3
        elif most_common + second_most_common == 4:
            return 2
        elif most_common == 2:
            return 1
        return 0

    def _count(self, cards):
        counter = Counter(cards)
        if self.use_jokers:
            counts = safe_list([c[1] for c in counter.most_common() if c[0] != "J"])
            return counts.get(0, 0) + counter.get("J", 0), counts.get(1, 0)
        counts = safe_list([c[1] for c in counter.most_common()])
        return counts.get(0, 0), counts.get(1, 0)

    def __repr__(self):
        return f"Hand<cards={self.cards}, type={self.type}>"

    def __lt__(self, other):
        return self.type < other.type or (self.type == other.type and self.cards < other.cards)


if __name__ == "__main__":
    plays = import_input("\n", str.split, example=False)

    hands = [Hand(cards, bid) for cards, bid in plays]
    winnings = sum([hand.bid * i for i, hand in enumerate(sorted(hands), 1)])
    print("Sum of winnings (without jokers):", c(winnings, Color.GREEN))

    hands = [Hand(cards, bid, True) for cards, bid in plays]
    winnings = sum([hand.bid * i for i, hand in enumerate(sorted(hands), 1)])
    print("Sum of winnings (with jokers):", c(winnings, Color.GREEN))
