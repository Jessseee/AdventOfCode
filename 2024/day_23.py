# Day 23 of Advent of Code 2024
# LAN Party

import unittest
from collections import defaultdict

from aoc.helpers import import_input, parse_input


def parser(inputs):
    edges = [line.split("-") for line in inputs.split("\n")]
    network = defaultdict(list)
    for node1, node2 in edges:
        network[node1].append(node2)
        network[node2].append(node1)
    return network


def find_maximally_connected_groups(network, current_node, num_nodes, groups=None, group=None):
    if group is None:
        group = {current_node}
    if groups is None:
        groups = []

    if len(group) == num_nodes:
        group = set(group)
        if group not in groups:
            groups.append(group)
        return groups

    for next_node in network[current_node]:
        if all(next_node in network[node] for node in group):
            find_maximally_connected_groups(network, next_node, num_nodes, groups, group | {next_node})

    return groups


def find_largest_maximally_connected_group(network, current_node, largest_group=None, group=None, visited=None):
    if group is None:
        group = {current_node}
    if visited is None:
        visited = {current_node}
        
    if largest_group is None or len(group) > len(largest_group):
        largest_group = group

    for next_node in network[current_node]:
        if next_node in visited:
            continue
        if all(next_node in network[node] for node in group):
            largest_group = find_largest_maximally_connected_group(
                network, next_node, largest_group, group | {next_node}, visited | {next_node}
            )

    return largest_group


@parse_input(parser)
def part1(network):
    groups = []
    for node in [node for node in network if node.startswith("t")]:
        for group in find_maximally_connected_groups(network, node, 3):
            if group not in groups:
                groups.append(group)
    return len(groups)


@parse_input(parser)
def part2(network):
    groups = []
    for node in network:
        groups.append(find_largest_maximally_connected_group(network, node))
    return ",".join(list(sorted(max(groups, key=len))))


class Tests202423(unittest.TestCase):
    inputs = (
        "kh-tc\nqp-kh\nde-cg\nka-co\nyn-aq\nqp-ub\ncg-tb\nvc-aq\ntb-ka\nwh-tc\nyn-cg\nkh-ub\nta-co\nde-co"
        "\ntc-td\ntb-wq\nwh-td\nta-ka\ntd-qp\naq-cg\nwq-ub\nub-vc\nde-ta\nwq-aq\nwq-vc\nwh-yn\nka-de\nkh-ta"
        "\nco-tc\nwh-qp\ntb-vc\ntd-yn"
    )

    def test_part1(self):
        expected = 7
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = "co,de,ka,ta"
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
