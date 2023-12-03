# Day 14 of Advent of Code 2021
# Chiton

# We've almost reached the exit of the cave, but the walls are getting closer together. Our submarine can barely still
# fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to
# bump any of them. The cavern is large, but has a very low ceiling, restricting our motion to two dimensions. a quick
# scan of chiton density produces a map of risk level throughout the cave. Our goal is to find the safest path through
# the cave with the lowest total risk score.

# We can use Dijkstra's algorithm to calculate the safest path through the cave. Using the risk score as the distance
# between nodes on a graph. We first generate a dictionary with all the nodes and their neighbours. We also create a
# list of all the nodes in the graph which are unvisited and set their risk score to be infinite. After which we start
# traversing the graph. Until the current node is our final target we keep searching for the path with the lowest
# risk. We compare the risk of the current node with the risk of their neighbours which is infinite until we have
# visited it and set it to be the sum of the risk of the current node and the unvisited neighbour. Once we reach the
# final target node we return the total risk score of the target node.

from collections import defaultdict
from heapq import heappop, heappush
from math import inf

import numpy as np

from aoc.helpers import *


def dijkstra(risk_map):
    x_max, y_max = (risk_map.shape[0] - 1, risk_map.shape[1] - 1)
    start = (0, 0)
    target = (x_max, y_max)

    cur_risk = 0
    scores = {(x, y): inf for (x, y), _ in np.ndenumerate(risk_map)}
    scores[start] = cur_risk
    visited = np.zeros(risk_map.shape, bool)
    to_visit = [(start, cur_risk)]
    while to_visit:
        (x, y), cur_risk = heappop(to_visit)
        neighbours = [(max(x - 1, 0), y), (min(x + 1, x_max), y), (x, max(y - 1, 0)), (x, min(y + 1, y_max))]
        visited[(x, y)] = True
        for neighbour in neighbours:
            if visited[neighbour]:
                continue
            new_risk = cur_risk + risk_map[neighbour]
            if scores[neighbour] > new_risk:
                scores[neighbour] = new_risk
                heappush(to_visit, (neighbour, new_risk))
    return scores[target]


if __name__ == "__main__":
    risk_map = np.array([list(map(int, line)) for line in import_input("\n", example=True)])
    large_risk_map = np.array(
        [[(risk - 1 + dx + dy) % 9 + 1 for dx in range(5) for risk in row] for dy in range(5) for row in risk_map]
    )

    print("The safest path on the small map has a total risk score of:", c(dijkstra(risk_map), 31))
    print("The safest path on the large map has a total risk score of:", c(dijkstra(large_risk_map), 31))
