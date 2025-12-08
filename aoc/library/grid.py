"""A small library of 2d-grid helper functions and search implementations."""

import heapq
from collections import deque
from math import inf
from typing import Callable

from aoc.library.tuples import add


def regular_directions(
        as_dict=False, names=("u", "r", "d", "l")
) -> list[tuple[int, int]] | dict:
    """
    Get the four basic directions in clockwise order.

    :param as_dict: Whether to return a dict with as key the names of the directions.
    :param names: The names to use when returning as a dict.
    :returns: up, right, down, left.
    """
    directions = (0, 1), (1, 0), (0, -1), (-1, 0)
    return {k: v for k, v in zip(names, directions)} if as_dict else directions


def cardinal_directions(
    as_dict=False, names=("n", "ne", "se", "s", "sw", "nw")
) -> dict[str: tuple[int, int]] | list[tuple[int, int]]:
    """
    Get all eight cardinal directions in clockwise order.

    :param as_dict: Whether to return a dict with as key the names of the directions.
    :param names: The names to use when returning as a dict.
    :returns: north, north_east, east, south_east, south, south_west, west, north_west.
    """
    directions = (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)
    return {k: v for k, v in zip(names, directions)} if as_dict else directions


def hexagonal_directions(
    as_dict=False, names=("n", "ne", "se", "s", "sw", "nw")
) -> dict[str: tuple[int, int]] | list[tuple[int, int]]:
    """
    Get all six hexagonal directions in clockwise order.
    source: https://www.redblobgames.com/grids/hexagons/#neighbors-axial

    :param as_dict: Whether to return a dict with as key the names of the directions.
    :param names: The names to use when returning as a dict.
    :returns: Directions (north, north_east, south_east, south, south_west, north_west).
    """
    directions = (0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)
    return {k: v for k, v in zip(names, directions)} if as_dict else directions


def manhattan_distance(
        a: tuple[int, ...], b: tuple[int, ...] = None
) -> int:
    """
    The Manhattan (taxi-driver) distance between two points.

    :param a: The first point.
    :param b: The second point, defaults to the origin.
    :returns: The manhattan distance between the two points.
    """
    b = b or tuple(0 for _ in range(len(a)))
    if len(a) != len(b):
        raise ValueError("To calculate distance 'a' and 'b' must be the same length.")
    return sum([abs(p - q) for p, q in zip(a, b)])


def euclidian_distance(
        a: tuple[int, ...], b: tuple[int, ...] = None
) -> int:
    """
    The Euclidian (straight-line) distance between two points.

    :param a: The first point.
    :param b: The second point, defaults to the origin.
    :returns: The manhattan distance between the two points.
    """
    b = b or tuple(0 for _ in range(len(a)))
    return sum([(p - q)**2 for p, q in zip(a, b)])**0.5


def get_neighbours(
        x: int | float, y: int | float, directions: list[tuple[int, int]] = None
) -> list[tuple[int, int]]:
    """Find neighbouring positions in a 2D grid."""
    directions = directions or regular_directions()
    return [add((x, y), direction) for direction in directions]


def get_neighbours_within_bound(
        x: int | float, y: int | float, directions: list[tuple[int, int]] = None, min_x=0, max_x=inf, min_y=0, max_y=inf
) -> list[tuple[int, int]]:
    """Find neighbouring positions in a 2D grid, given bounding values of x and y."""
    directions = directions or regular_directions()
    neighbours = [add((x, y), direction) for direction in directions]
    return [(x, y) for x, y in neighbours if min_x <= x < max_x and min_y <= y < max_y]


def reconstruct_path(
        connections: dict[tuple[int, int]], current: tuple[int, int]
) -> list[tuple[int, int]]:
    """Reconstruct a path from a directional graph."""
    shortest_path = [current]
    while current in connections:
        current = connections[current]
        shortest_path.insert(0, current)
    return shortest_path


def a_star_search(
        start: tuple[int, int],
        target: tuple[int, int],
        weights: list[list[int]] | dict[tuple[int, int], int] | Callable[[tuple[int, int]], int] = None,
        heuristic=manhattan_distance,
        neighbours=get_neighbours
) -> list[tuple[int, int]]:
    """
    Implementation of the A* search algorithm.

    :param start: A starting node.
    :param target: A target node.
    :param weights: A function, dict or 2d array to retrieve the weights of the nodes.
    :param heuristic: A function to estimates the cost of a path.
    :param neighbours: A function to determine the neighbours of a node.
    """
    connections = {}
    heapq.heappush(to_visit := [], (0, start))
    g_score = {start: 0}

    while len(to_visit) > 0:
        _, current = heapq.heappop(to_visit)
        if current == target:
            return reconstruct_path(connections, current)
        for neighbour in neighbours(*current):
            cost = 1
            if callable(weights):
                cost = weights(*neighbour)
            elif isinstance(weights, dict):
                cost = weights[neighbour]
            elif isinstance(weights, list):
                cost = weights[neighbour[1]][neighbour[0]]
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score.get(neighbour, inf):
                connections[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbour, target)
                if neighbour not in to_visit:
                    heapq.heappush(to_visit, (f_score, neighbour))


def dijkstra_search(
        start: tuple[int, int],
        target: tuple[int, int],
        weights: list[list[int]] | dict[tuple[int, int], int] | Callable[[tuple[int, int]], int] = None,
        neighbours=get_neighbours,
) -> list[tuple[int, int]]:
    """
    Implementation of the Dijkstra search algorithm.

    :param start: A starting node.
    :param target: A target node.
    :param weights: A function, dict or 2d array to retrieve the weights of the nodes.
    :param neighbours: A function to determine the neighbours of a node.
    """
    connections = {}
    heapq.heappush(to_visit := [], (0, start))
    g_score = {start: 0}

    while len(to_visit) > 0:
        current_g_score, current = heapq.heappop(to_visit)
        if current == target:
            return reconstruct_path(connections, current)
        for neighbour in neighbours(*current):
            cost = 1
            if callable(weights):
                cost = weights(*neighbour)
            elif isinstance(weights, dict):
                cost = weights[neighbour]
            elif isinstance(weights, list):
                cost = weights[neighbour[1]][neighbour[0]]
            tentative_g_score = current_g_score + cost
            if tentative_g_score < g_score.get(neighbour, inf):
                connections[neighbour] = current
                g_score[neighbour] = tentative_g_score
                if neighbour not in to_visit:
                    heapq.heappush(to_visit, (tentative_g_score, neighbour))


def breadth_first_search(
        start: tuple[int, int],
        target: tuple[int, int],
        neighbours=get_neighbours
) -> list[tuple[int, int]]:
    """
    Implementation of Breadth First Search (BFS).

    :param start: A starting node.
    :param target: A target node.
    :param neighbours: A function to determine the neighbours of a node.
    """
    to_visit = deque([start])
    explored = {start}
    connections = {}
    while len(to_visit):
        current = to_visit.pop()
        if current == target:
            return reconstruct_path(connections, current)
        for neighbour in neighbours(*current):
            if neighbour not in explored:
                explored.add(neighbour)
                connections[neighbour] = current
                to_visit.appendleft(neighbour)


def depth_first_search(
        start: tuple[int, int],
        target: tuple[int, int],
        neighbours=get_neighbours
) -> list[tuple[int, int]]:
    """
    Implementation of Depth First Search (DFS).

    :param start: A starting node.
    :param target: A target node.
    :param neighbours: A function to determine the neighbours of a node.
    """
    to_visit = deque([start])
    explored = {start}
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


def flood_fill(
        start: tuple[int, int],
        max_distance: int = None,
        neighbours=get_neighbours
) -> set[tuple[int, int]]:
    """
    Modification of the BFS algorithm to return all the explored points (up to a maximum distance).

    :param start: A starting node.
    :param max_distance: The maximum number of steps away from the starting node to explore.
    :neighbours: A function to determine the neighbours of a node.
    """
    to_visit = deque([(0, start)])
    explored = {start}
    while len(to_visit):
        distance, current = to_visit.pop()
        for neighbour in neighbours(*current):
            if neighbour in explored:
                continue
            if max_distance and distance <= max_distance + 1:
                explored.add(neighbour)
                to_visit.append((distance + 1, neighbour))
    return explored
