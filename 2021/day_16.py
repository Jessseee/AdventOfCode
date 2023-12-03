# Day 16 of Advent of Code 2021
# Packet Decoder

# As we leave the cave and reach open waters, we receive a transmission from the Elves back on the ship.
# The transmission was sent using the Buoyancy Interchange Transmission System (BITS), a method of packing
# numeric expressions into a binary sequence. Your submarine's computer has saved the transmission in
# hexadecimal but unfortunately the decoder seems to be broken. We will have to decode the message ourselves.

# DECODING
# The first step of decoding the message is to convert the hexadecimal representation into binary.
# Each character of hexadecimal corresponds to four bits of binary data. The BITS transmission contains a
# single packet at its outermost layer which itself contains many other packets. The hexadecimal representation
# of this packet might encode a few extra 0 bits at the end as padding for the hexadecimal representation.

# LITERAL PACKET
# Packets with type ID 4 represent a literal value. Literal value packets encode a single binary number.
# To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits,
# and then it is broken into groups of four bits. Each group is prefixed by a 1 bit except the last group,
# which is prefixed by a 0 bit.

# OPERATOR PACKET
# Every other type of packet (any packet with a type ID other than 4) represent an operator that performs
# some calculation on one or more sub-packets contained within. An operator packet contains one or more packets.
# The packet type IDs represent the following operator types: 0: sum, 1: product, 2: minimum, 3: maximum,
# 5: greater than, 6: less than, 7: equal to.

# To indicate which subsequent binary data represents its sub-packets, an operator packet can use one of
# two modes indicated by the bit immediately after the packet header; this is called the length type ID:
#   - If the length type ID is 0, then the next 15 bits are a number that represents
#     the total length in bits of the sub-packets contained by this packet.
#   - If the length type ID is 1, then the next 11 bits are a number that represents
#     the number of sub-packets immediately contained by this packet.
# Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.

import numpy as np

from aoc.helpers import *


class Packet:
    def __init__(self, bits):
        self.bits = bits

        self.pointer = 0
        self.value = 0
        self.sub_packets = []

        self.version = self.get_bits(3, True)
        self.type = self.get_bits(3, True)
        self.type_id = None if self.type == 4 else self.get_bits(1)

        global operators
        self.operator = operators[self.type]

        global total_version
        total_version += self.version

        self.value = self.literal_from_binary() if self.type == 4 else self.operator_from_binary()

    def print(self, depth=0):
        if self.type == 4:
            print("\t" * depth + f"<num v={self.value}/>")
        else:
            print("\t" * depth + f"<{self.operator.__name__} t={self.type_id}")
            for packet in self.sub_packets:
                packet.print(depth + 1)
            print("\t" * depth + f"</{self.operator.__name__} v={self.value}>>")

    # Pop a number of bits off of the packet's binary
    def get_bits(self, length, to_int=False):
        bits = self.bits[self.pointer : self.pointer + length]
        self.pointer += length
        return int(bits, 2) if to_int else bits

    def literal_from_binary(self):
        number = ""
        while True:
            start = self.get_bits(1)
            number += self.get_bits(4)
            if start == "0":
                value = int(number, 2)
                break
        self.bits = self.bits[: self.pointer]
        return value

    def operator_from_binary(self):
        values = []

        # If length type ID is 0 then the next 15 bits are the length of the sub-packet
        if self.type_id == "0":
            sub_packet_length = self.get_bits(15, True)
            while sub_packet_length > 0:
                sub_packet = Packet(self.bits[self.pointer : self.pointer + sub_packet_length])
                values.append(sub_packet.value)
                self.sub_packets.append(sub_packet)
                self.pointer += sub_packet.pointer
                sub_packet_length -= sub_packet.pointer

        # If length type ID is 1 then the next 11 bits are the number of sub-packets
        elif self.type_id == "1":
            nr_sub_packets = self.get_bits(11, True)
            for _ in range(nr_sub_packets):
                sub_packet = Packet(self.bits[self.pointer :])
                values.append(sub_packet.value)
                self.sub_packets.append(sub_packet)
                self.pointer += sub_packet.pointer

        # apparently np.prod can have an integer overflow :(
        if self.operator == np.prod:
            value = self.operator(values, dtype=np.int64)
        elif self.type < 4:
            value = self.operator(values)
        else:
            value = self.operator(*values)

        self.bits = self.bits[: self.pointer]
        return value


if __name__ == "__main__":
    bits = "".join(["{0:04b}".format(int(char, 16)) for char in import_input(example=False).read()])
    operators = [np.sum, np.prod, np.min, np.max, int, np.greater, np.less, np.equal]
    total_version = 0
    outer_packet = Packet(bits)
    outer_packet.print()
    print("\nresult:", outer_packet.value)
    print("total version:", total_version)
