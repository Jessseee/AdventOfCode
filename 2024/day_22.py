# Day 22 of Advent of Code 2024
# Monkey Market

import unittest

from tqdm import tqdm

from aoc.helpers import import_input, parse_input


def parser(inputs):
    return list(map(int, inputs.split("\n")))


def get_secrets(secret):
    secrets = []
    for _ in range(2000):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        secrets.append(secret)
    return secrets


@parse_input(parser)
def part1(secrets):
    return sum(get_secrets(secret)[-1] for secret in secrets)


@parse_input(parser)
def part2(secrets):
    buyers = []
    for init_secret in secrets:
        prices = [init_secret % 10]
        changes = [None]
        sequences = {}
        for i, secret in enumerate(get_secrets(init_secret), 1):
            prices.append(secret % 10)
            changes.append(prices[i-1] - prices[i])
            if (sequence := tuple(changes[i-3:i+1])) not in sequences:
                sequences[sequence] = prices[i]
        buyers.append(sequences)

    best = 0
    seen = set()
    pbar = tqdm(buyers)
    for cur_sequences in pbar:
        for sequence, cur_price in cur_sequences.items():
            if sequence in seen:
                continue
            seen.add(sequence)
            total = cur_price
            for other_sequences in buyers:
                if cur_sequences == other_sequences:
                    continue
                if other_price := other_sequences.get(sequence):
                    total += other_price
            if total > best:
                best = total
                pbar.set_postfix({"best": (best, sequence)})
    return best


class Tests202422(unittest.TestCase):
    def test_part1(self):
        inputs = "1\n10\n100\n2024"
        expected = 37327623
        self.assertEqual(expected, part1(inputs))

    def test_part2(self):
        inputs = "1\n2\n3\n2024"
        expected = 23
        self.assertEqual(expected, part2(inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
