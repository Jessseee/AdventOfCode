import operator
from functools import reduce


def map(*tuples: list[tuple[int, ...]], opp) -> tuple[int, ...]:
    """
    Apply an operation to a zip of each value of a number of tuples.
    By default, adds the values of the tuples.

    :param tuples: The tuples of which to sum the values.
    :param opp: The operation to apply to the two tuples.
    :returns: A tuple of the processed values.
    """
    return tuple(reduce(opp, x) for x in zip(*tuples))


def add(*tuples: list[tuple[int, ...]]) -> tuple[int, ...]:
    """
    Add together all values of a series of tuples.

    :param tuples: The tuples of which to sum the values.
    :returns: A tuple of the subtracted values.
    """
    return map(*tuples, opp=operator.add)


def sub(*tuples: list[tuple[int, ...]]) -> tuple[int, ...]:
    """
    Subtract all values of a series of tuples.

    :param tuples: The tuples of which to subtract the values.
    :returns: A tuple of the added values.
    """

    return map(*tuples, opp=operator.sub)


def mul(*tuples: list[tuple[int, ...]]) -> tuple[int, ...]:
    """
    Multiply all values of a series of tuples.

    :param tuples: The tuples of which to multiply the values.
    :returns: A tuple of the multiplied values.
    """

    return map(*tuples, opp=operator.mul)


def rot90(vector: tuple[int, int], clockwise: bool = True) -> tuple[int, int]:
    """
    Rotate a 2d vector +/- 90 degrees around the Z axis.

    :param vector: The vector to rotate.
    :param clockwise: Whether to turn clockwise.
    :returns: The rotated vector.
    """
    return (vector[1], -vector[0]) if clockwise else (-vector[1], vector[0])


class safe_list(list):
    """Subclass of build-in list with safe get() method."""

    def get(self, index: int, default=None):
        """Return the value for key if key is in the dictionary, else default."""
        try:
            return self.__getitem__(index)
        except IndexError:
            return default
