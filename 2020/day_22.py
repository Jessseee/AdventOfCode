# Day Advent of Code
# Crab Cards Combat
import copy
from collections import deque
from itertools import islice

from aoc.helpers import *


def display_decks(decks, round_nr, game=None):
    if game:
        print(f"-- Round {round_nr} {c(f'(Game {game})' , 30+game)} --")
    else:
        print(f"-- Round {round_nr} --")
    for i, deck in enumerate(decks):
        print(f"Player {i + 1}'s deck: {list(deck)}")
    print()


def calc_winner_score(winner_idx, winner_deck):
    score = sum([card * i for i, card in enumerate(reversed(winner_deck), start=1)])
    print(c(f"\nPLAYER {winner_idx + 1} WON THE GAME [{score} points]", 32))
    return score


def play_regular_combat(decks, display_rounds=True):
    round_nr = 1

    if display_rounds:
        display_decks(decks, round_nr)

    # Play rounds until only one player holds all the cards
    while len([deck for deck in decks if deck]) > 1:
        cur_round = [deck.popleft() for deck in decks if deck]
        decks[cur_round.index(max(cur_round))].extend(sorted(cur_round, reverse=True))
        round_nr += 1

        if display_rounds:
            display_decks(decks, round_nr)

    # Determine winner
    winner_deck = list(filter(None, decks))[0]
    winner_idx = decks.index(winner_deck)

    return winner_idx, winner_deck


def play_recursive_combat(decks, display_rounds=True, game=1):
    print(c(f"=== GAME {game} ===", 33))

    winner_idx = 0
    score = 0
    round_nr = 1
    cache = []

    if display_rounds:
        display_decks(decks, round_nr, game)

    # Play rounds until only one player holds all the cards
    while len([deck for deck in decks if deck]) > 1:
        cur_round = [deck.popleft() for deck in decks if deck]

        # If current round has already been played player 1 wins
        if decks in cache:
            print(
                c(f"Player {winner_idx + 1} won recursive game {game} Because the last deck was already played\n", 32)
            )
            return winner_idx, score
        else:
            cache.append(copy.deepcopy(decks))

        # If both players have enough cards start another recursive game of Combat
        if all(len(decks[i]) >= card for i, card in enumerate(cur_round)):
            decks_copy = [deque(islice(decks[i], 0, card)) for i, card in enumerate(cur_round)]
            winner_idx, _ = play_recursive_combat(decks_copy, display_rounds, game + 1)
            decks[winner_idx].append(cur_round.pop(winner_idx))
            decks[winner_idx].extend(cur_round)
        else:
            decks[cur_round.index(max(cur_round))].extend(sorted(cur_round, reverse=True))
        round_nr += 1

        if display_rounds:
            display_decks(decks, round_nr, game)

    # Determine winner
    winner_deck = list(filter(None, decks))[0]
    winner_idx = decks.index(winner_deck)

    print(c(f"Player {winner_idx + 1} won recursive game {game}\n", 32))
    return winner_idx, winner_deck


if __name__ == "__main__":
    decks = import_input().read().split("\n\n")
    decks = [deque(map(int, deck.split(":\n")[1].split("\n"))) for deck in decks]

    print(c("\nPLAYING REGULAR COMBAT", 35))
    winner_idx, winner_deck = play_regular_combat(copy.deepcopy(decks), False)
    calc_winner_score(winner_idx, winner_deck)

    print(c("\nPLAYING RECURSIVE COMBAT", 36))
    winner_idx, winner_deck = play_recursive_combat(copy.deepcopy(decks))
    calc_winner_score(winner_idx, winner_deck)
