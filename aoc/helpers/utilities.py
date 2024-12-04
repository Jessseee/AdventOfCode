import bisect
import operator
from collections import deque
from functools import reduce
from math import inf


def map_tuples(*tuples: list[tuple[int, ...]], opp) -> tuple[int, ...]:
    """
    Apply an operation to a zip of each value of a number of tuples.
    By default, adds the values of the tuples.

    :param tuples: The tuples of which to sum the values.
    :param opp: The operation to apply to the two tuples.
    :returns: A tuple of the processed values.
    """
    return tuple(reduce(opp, x) for x in zip(*tuples))


def add_tuples(*tuples: list[tuple[int, ...]]) -> tuple[int, ...]:
    """
    Add together all values of a series of tuples.

    :param tuples: The tuples of which to sum the values.
    :returns: A tuple of the subtracted values.
    """
    return map_tuples(*tuples, opp=operator.add)


def sub_tuples(*tuples: list[tuple[int, ...]]) -> tuple[int, ...]:
    """
    Subtract all values of a series of tuples.

    :param tuples: The tuples of which to subtract the values.
    :returns: A tuple of the added values.
    """

    return map_tuples(*tuples, opp=operator.sub)


def mul_tuples(*tuples: list[tuple[int, ...]]) -> tuple[int, ...]:
    """
    Multiply all values of a series of tuples.

    :param tuples: The tuples of which to multiply the values.
    :returns: A tuple of the multiplied values.
    """

    return map_tuples(*tuples, opp=operator.mul)


def rotate90(vector: tuple[int, int], clockwise: bool = True) -> tuple[int, int]:
    """
    Rotate a 2d vector +/- 90 degrees around the Z axis.

    :param vector: The vector to rotate.
    :param clockwise: Whether to turn clockwise.
    :returns: The rotated vector.
    """
    return (vector[1], -vector[0]) if clockwise else (-vector[1], vector[0])


def regular_directions(as_dict=False, names=("u", "r", "d", "l")) -> list[tuple[int, int]] | dict:
    """
    Get the four directions in clockwise order.

    :param as_dict: Whether to return a dict with as key the names of the directions.
    :param names: The names to use when returning as a dict.
    :returns: up, right, down, left.
    """
    dirs = (0, 1), (1, 0), (0, -1), (-1, 0)
    return {k: v for k, v in zip(names, dirs)} if as_dict else dirs


def cardinal_directions(
    as_dict=False, names=("n", "ne", "se", "s", "sw", "nw")
) -> dict[str : tuple[int, int]] | list[tuple[int, int]]:
    """
    Get all eight cardinal directions in clockwise order.

    :param as_dict: Whether to return a dict with as key the names of the directions.
    :param names: The names to use when returning as a dict.
    :returns: north, north_east, east, south_east, south, south_west, west, north_west.
    """
    dirs = (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)
    return {k: v for k, v in zip(names, dirs)} if as_dict else dirs


def hexagonal_directions(
    as_dict=False, names=("n", "ne", "se", "s", "sw", "nw")
) -> dict[str : tuple[int, int]] | list[tuple[int, int]]:
    """
    Get all six hexagonal directions in clockwise order.
    source: https://www.redblobgames.com/grids/hexagons/#neighbors-axial

    :param as_dict: Whether to return a dict with as key the names of the directions.
    :param names: The names to use when returning as a dict.
    :returns: Directions (north, north_east, south_east, south, south_west, north_west).
    """
    dirs = (0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)
    return {k: v for k, v in zip(names, dirs)} if as_dict else dirs


def manhattan_distance(a: tuple[int, ...], b: tuple[int, ...] = None) -> int:
    """
    The manhattan (taxi-driver) distance between two points.

    :param a: The first point.
    :param b: The second point, defaults to the origin.
    :returns: The manhattan distance between the two points.
    """
    b = b or tuple(0 for _ in range(len(a)))
    if len(a) != len(b):
        raise ValueError("To calculate distance 'a' and 'b' must be the same length.")
    return sum([abs(p - q) for p, q in zip(a, b)])


def get_neighbours(x: int | float, y: int | float, directions: list[tuple[int, int]] = None) -> list[tuple[int, int]]:
    """Find neighbouring positions in a 2D grid."""
    directions = directions or regular_directions()
    return [add_tuples((x, y), direction) for direction in directions]


def get_neighbours_within_bound(
    x: int | float, y: int | float, directions: list[tuple[int, int]] = None, min_x=0, max_x=inf, min_y=0, max_y=inf
) -> list[tuple[int, int]]:
    """Find neighbouring positions in a 2D grid, given bounding values of x and y."""
    directions = directions or regular_directions()
    neighbours = [add_tuples((x, y), direction) for direction in directions]
    return [(x, y) for x, y in neighbours if min_x <= x < max_x and min_y <= y < max_y]


def reconstruct_path(connections: dict[tuple[int, int]], current: tuple[int, int], target: tuple[int, int] = None):
    """
    Reconstruct a path from a directional graph.
    """
    shortest_path = [current]
    while current in connections:
        current = connections[current]
        shortest_path.insert(0, current)
        if target and current == target:
            break
    return shortest_path


def a_star_search(
    start: tuple[int, int],
    target: tuple[int, int],
    weights: list[list[int]],
    distance=manhattan_distance,
    neighbours=get_neighbours,
) -> list[tuple[int, int]]:
    """
    Implementation of the A* search algorithm.

    :param start: A starting node.
    :param target: A target node.
    :param weights: A 2D array of weights for the nodes.
    :param distance: A function to estimates the cost of a path.
    :param neighbours: A function to determine the neighbours of a node.
    """
    current = start
    connections = {}
    to_visit = {current}
    g_score = {current: 0}
    f_score = {current: weights[current]}

    while len(to_visit) > 0:
        d = {node: f_score[node] for node in to_visit}
        current = min(d, key=d.get)
        if current == target:
            return reconstruct_path(connections, current)
        to_visit.remove(current)
        for neighbour in neighbours(*current):
            tentative_g_score = g_score[current] + weights[neighbour]
            if tentative_g_score < g_score.get(neighbour, inf):
                connections[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + distance(neighbour, target)
                if neighbour not in to_visit:
                    bisect.insort(to_visit, neighbour, key=lambda n: f_score[n])


def breadth_first_search(start, target, neighbours=get_neighbours):
    to_visit = deque([start])
    explored = set(start)
    connections = {}
    while len(to_visit):
        current = to_visit.pop()
        if current == target:
            return reconstruct_path(connections, current)
        for neighbour in neighbours(*current):
            if neighbour not in explored:
                explored.add(neighbour)
                connections[neighbour] = current
                to_visit.append(neighbour)


class safe_list(list):
    """Subclass of build-in list with safe get() method."""

    def get(self, index: int, default=None):
        """Return the value for key if key is in the dictionary, else default."""
        try:
            return self.__getitem__(index)
        except IndexError:
            return default
