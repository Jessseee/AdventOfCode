# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
import re

from aoc.helpers import *


def check_tls(ip):
    hypernet_sequences = re.findall(r"\[[a-z]+\]", ip)
    pattern = r"(?=([a-z])([a-z])\2\1)"
    for sequence in hypernet_sequences:
        if bool(re.search(pattern, sequence)):
            return False
    abba = re.findall(pattern, ip)
    return any([a != b for a, b in abba if abba != []])


def check_ssl(ip):
    hypernet_sequences = re.findall(r"\[[a-z]+\]", ip)
    pattern = r"(?=([a-z])([a-z])\1)"
    bab = []
    rest_ip = ip
    for sequence in hypernet_sequences:
        rest_ip = rest_ip.replace(sequence, "")
        bab += [(b, a) for b, a in re.findall(pattern, sequence) if b != a]
    aba = [(a, b) for a, b in re.findall(pattern, rest_ip) if a != b]
    return any([(b, a) in bab for a, b in aba])


if __name__ == "__main__":
    inputs = import_input("\n")
    valid_tls = 0
    valid_ssl = 0
    for ip in inputs:
        valid_tls += check_tls(ip)
        valid_ssl += check_ssl(ip)
    print("IPs that support TLS:", valid_tls)
    print("IPs that support SSL:", valid_ssl)
