# Day 13 of Advent of Code 2022
# Distress Signal

# At the top of the mountain our communication device suddenly receives a distress signal. However, the packets seem
# to be out of order. Our job is to first find which pairs of packets are already in the right order and then sort
# all the packets into a correct signal. Finally, we can find a decoder key for the signal by sorting in two divider
# packets and multiplying their indices.

from helpers import *
from functools import cmp_to_key


def parse_packets(packets):
    return[eval(packet) for packet in packets.split('\n')]


def compare_lists(left_list, right_list, depth=0):
    if left_list == right_list: return 0
    for i, left in enumerate(left_list):
        if i >= len(right_list): return 1
        right = right_list[i]
        order = compare_items(left, right, depth)
        if order == 0:
            continue
        return order
    return -1


def compare_items(left, right, depth=0):
    if isinstance(left, int) and isinstance(right, int):
        if left == right: return 0
        if left < right: return -1
        return 1
    if isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right, depth + 1)
    if isinstance(left, int):
        return compare_lists([left], right, depth + 1)
    if isinstance(right, int):
        return compare_lists(left, [right], depth + 1)


if __name__ == '__main__':
    packet_pairs = import_input('\n\n', parse_packets, example=True)
    correct_packets = sum([i+1 for i, (left, right) in enumerate(packet_pairs) if compare_items(left, right) == -1])
    print(f"Number of packets in the right order: {result(correct_packets)}")

    all_packets = sum(packet_pairs, []) + [[[2]], [[6]]]
    sorted_packets = sorted(all_packets, key=cmp_to_key(compare_items))
    decoder_key = (sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1)
    print(f"The distress signal decoder key: {result(decoder_key)}")
