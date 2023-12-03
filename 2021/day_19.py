# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from itertools import combinations, permutations

import matplotlib.pyplot as plt
import numpy as np

from aoc.helpers import *


def intersection(beacon1, beacon2):
    return beacon1 == beacon2 or len(set(beacon1) & set(beacon2)) >= 3


def compare(p1, p2):
    if p2 == p1:
        return 1
    elif p2 == -p1:
        return -1
    else:
        return 0


def basis_diff(base, to_compare):
    x, y, z = base
    basis = []
    for p in to_compare:
        basis.append(np.array((compare(x, p), compare(y, p), compare(z, p))))
    return basis


if __name__ == "__main__":
    scanners = [
        [tuple(map(int, beacon.split(","))) for beacon in scanner.split("\n")[1:]]
        for scanner in import_input("\n\n", example=True)
    ]
    for i, scanner in enumerate(scanners):
        print(f"--- scanner {i} ---", scanner)
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        ax.scatter3D(0, 0, 0, color="red")
        for beacon in scanner:
            ax.scatter3D(*beacon, alpha=0.8, color="blue")
        plt.title(f"--- scanner {i} ---")
        # plt.show()

    # First calculate the distances between every beacon for each scanner
    scanner_beacon_dists = []
    for scanner in scanners:
        dists = {}
        for beacon in scanner:
            dists[beacon] = []
            for other_beacon in scanner:
                if beacon != other_beacon:
                    dists[beacon].append(np.linalg.norm(np.array(beacon) - np.array(other_beacon)))
        scanner_beacon_dists.append(dists)

    # Now match any scanners with the same distances
    scanner_matching_beacons = {}
    scanner_combinations = combinations(range(len(scanners)), 2)
    for i, j in scanner_combinations:
        matching_beacons = []
        for beacon, dist in scanner_beacon_dists[i].items():
            for other_beacon, other_dists in scanner_beacon_dists[j].items():
                if beacon == other_beacon:
                    continue
                if intersection(dist, other_dists):
                    matching_beacons.append((beacon, other_beacon))
        if len(matching_beacons) >= 12:
            scanner_matching_beacons[(i, j)] = matching_beacons

    print()
    scanner_rel_base = {}
    for key, matches in scanner_matching_beacons.items():
        match1, match2 = matches[:2]
        base = np.array(match1[0]) - np.array(match2[0])
        to_compare = np.array(match1[1]) - np.array(match2[1])
        basis = basis_diff(base, to_compare)
        x, y, z = basis[0] * match1[1], basis[1] * match1[1], basis[2] * match1[1]
        x, y, z = x[x.nonzero()][0], y[y.nonzero()][0], z[z.nonzero()][0]
        print(key, basis, match1[0] - np.array([x, y, z]))
        scanner_rel_base[key] = (match1[0] - np.array([x, y, z]), basis)
    # print(scanner_rel_base)
