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

from helpers import *
import numpy as np


class Packet:
    def __init__(self, bits):
        self.bits = bits
        self.consumed = 0
        self.value = 0

        self.version = self.consume(3, True)
        self.type = self.consume(3, True)

        global operators
        self.operator = operators[self.type]

        global total_version
        total_version += self.version

    # Pop a number of bits off of the packet's binary
    def consume(self, length, to_int=False):
        bits = self.bits[:length]
        self.bits = self.bits[length:]
        self.consumed += length
        return int(bits, 2) if to_int else bits

    def read(self, indent=0):
        # Packets with type 4 are literals
        if self.type == 4:
            number = ''
            while True:
                start = self.consume(1)
                number += self.consume(4)
                if start == '0':
                    self.value = int(number, 2)
                    break
            print('\t'*indent + f"<Packet t={self.type}, o=literal, v={self.value}, b={number}>")

        # Any other packets are operators
        else:
            values = []
            print('\t'*indent + f"<Packet t={self.type}, o={self.operator.__name__}>")

            # If length type ID is 0 then the next 15 bits are the length of the sub-packet
            if self.consume(1) == '0':
                sub_packet_length = self.consume(15, True)
                while sub_packet_length > 0:
                    sub_packet = Packet(self.bits[:sub_packet_length])
                    values.append(sub_packet.read(indent+1))
                    self.consume(sub_packet.consumed)
                    sub_packet_length -= sub_packet.consumed

            # If length type ID is 1 then the next 11 bits are the number of sub-packets
            else:
                nr_sub_packets = self.consume(11, True)
                for i in range(nr_sub_packets):
                    sub_packet = Packet(self.bits)
                    values.append(sub_packet.read(indent+1))
                    self.consume(sub_packet.consumed)

            # apparently np.prod can have an integer overflow :(
            if self.operator == np.prod:
                self.operator(values, dtype=np.int64)
            elif self.type < 4:
                self.value = self.operator(values)
            else:
                self.operator(*values)
            print('\t'*indent + f"</Packet t={self.type}, o={self.operator.__name__}, v={self.value}>")
        return self.value


if __name__ == '__main__':
    bits = ''.join(['{0:04b}'.format(int(char, 16)) for char in import_input(example=False).read()])
    operators = [np.sum, np.prod, np.min, np.max, int, np.greater, np.less, np.equal]
    total_version = 0
    packet = Packet(bits)
    result = packet.read()
    print('\nresult:', result)
    print('total version:', total_version)
