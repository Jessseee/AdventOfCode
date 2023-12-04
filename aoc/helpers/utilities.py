import operator
from functools import reduce


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


def regular_directions(as_dict=False, names=("u", "r", "d", "l")) -> list[tuple[int, int]]:
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
