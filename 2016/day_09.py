# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from helpers import *


def decompress(in_file, v2=False):
    i = 0
    out_file = ""
    while i < len(in_file):
        if in_file[i] == "(":
            marker, residual = in_file[i:].split(")", 1)
            length, n = list(map(int, marker[1:].split("x")))
            sequence = residual[:length]*n
            if v2:
                while "(" in sequence:
                    sequence = decompress(sequence)
            out_file += sequence
            i += len(marker) + length + 1
        else:
            out_file += in_file[i]
            i += 1
    return out_file


def calc_decompressed_size(file, v2=False):
    i = 0
    length = 0
    while i < len(file):
        if file[i] == "(":
            marker, residual = file[i:].split(")", 1)
            seq, n = list(map(int, marker[1:].split("x")))
            if v2 and '(' in residual[:seq]:
                length += calc_decompressed_size(residual[:seq]) * n
            else:
                length += seq * n
            i += len(marker) + seq + 1
        else:
            length += 1
            i += 1
    return length


if __name__ == '__main__':
    inputs = import_input('\n', example=False)
    for file in inputs:
        decompressed_v1 = decompress(file)
        # print("input:\n", file)
        # print("decompress_v1 output:\n", decompressed_v1)
        print("decompress_v1 output length:", calc_decompressed_size(file))

        # Whoops, decompress v2 is way too slow for the large input...
        # decompressed_v2 = decompress(file, v2=True)
        # print("decompress_v2 output:\n", decompressed_v2)

        # Just calculate the uncompressed size instead
        print("decompress_v2 output length:", calc_decompressed_size(file, v2=True))
