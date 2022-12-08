# A class to store and manipulate n-dimensional vectors.

class Vector:
    """ A class to represent an n-dimensional vector. """

    NR_DIMS = None

    def __init__(self, *dims: int | float) -> "Vector":
        """ :param dims: An arbitrary number of dimensional positions. """
        self.dims = dims

    def __len__(self):
        return len(self.dims)

    def __getitem__(self, key: int) -> int | float:
        return self.dims[key]

    def __iter__(self):
        return iter(self.dims)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            dims = (self[i] + other for i in range(len(self)))
            return self.__class__(*dims)
        elif isinstance(other, Vector):
            self.__check_dims(other)
            dims = (self[i] + other[i] for i in range(len(self)))
            return self.__class__(*dims)
        raise NotImplementedError(f"Addition of {self.__class__} with {other.__class__} is not implemented.")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            dims = (self[i] - other for i in range(len(self)))
            return self.__class__(*dims)
        elif isinstance(other, Vector):
            self.__check_dims(other)
            dims = (self[i] - other[i] for i in range(len(self)))
            return self.__class__(*dims)
        raise NotImplementedError(f"Subtraction of {self.__class__} with {other.__class__} is not implemented.")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            dims = (self[i] * other for i in range(len(self)))
            return self.__class__(*dims)
        elif isinstance(other, Vector):
            self.__check_dims(other)
            dims = (self[i] * other[i] for i in range(len(self)))
            return self.__class__(*dims)
        raise NotImplementedError(f"Multiplication of {self.__class__} with {other.__class__} is not implemented.")

    def __repr__(self):
        return f"<{', '.join(map(str, self))}>"

    def __hash__(self):
        return self.dims.__hash__()

    def __eq__(self, other: "Vector") -> bool:
        self.__check_dims(other)
        return tuple(self) == tuple(other)

    def __check_dims(self, other: "Vector") -> None:
        """ Check if the length of another Vector is equal to this Vector. """
        if len(self) != len(other):
            raise ValueError("Trying to do an operation on vectors of different sizes.")

    def dist_manhattan(self, other: "Vector" = None) -> float:
        """ Get the distance to some other Vector in Manhattan (or taxicab) geometry. """
        other = other or self.__class__.zeros()
        return sum([abs(p - q) for p, q in zip(self.dims, other.dims)])

    def dist_euclidean(self, other: "Vector" = None) -> float:
        """ Get the distance to some other Vector in Euclidian geometry. """
        other = other or self.__class__.zeros()
        return sum([abs(p - q) ** 2 for p, q in zip(self.dims, other.dims)]) ** (1/2)

    @classmethod
    def zeros(cls, **kwargs) -> "Vector":
        """ Initialise a zero Vector. """
        nr_dims = cls.NR_DIMS or kwargs.get('dims')
        if nr_dims is None: raise ValueError("Please provide a number of dimensions with the 'dims' keyword.")
        return cls(*(0 for _ in range(nr_dims)))

    @classmethod
    def full(cls, constant: int | float, **kwargs) -> "Vector":
        """ Initialise a Vector with a constant value. """
        nr_dims = cls.NR_DIMS or kwargs.get('dims')
        if nr_dims is None: raise ValueError("Please provide a number of dimensions with the 'dims' keyword.")
        return cls(*(constant for _ in range(nr_dims)))


class Matrix(Vector):
    """ Alias of the Vector class. """
    def __init__(self, *dims: int | float) -> "Matrix":
        super().__init__(*dims)


class MetaVector2D(type):
    DIRECTIONS = {
        'up': (0, 1), 'right': (1, 0), 'down': (0, -1), 'left': (-1, 0)
    }
    CARDINALS = {
        'north': (0, 1), 'north_east': (1, 1), 'east': (1, 0), 'south_east': (1, -1),
        'south': (0, -1), 'south_west': (-1, -1), 'west': (-1, 0), 'north_west': (-1, 1)
    }

    def __getattr__(cls, key):
        index = cls.DIRECTIONS.get(key) or cls.CARDINALS.get(key)
        if index is not None:
            return lambda: Vector2D(*cls.ALL_DIRECTIONS[index])
        raise AttributeError(key)

    def directions(cls) -> list["Vector2D"]:
        """:returns: Four directions (up, right, down, left)"""
        return [Vector2D(*direction) for direction in cls.DIRECTIONS.values()]

    def cardinals(cls):
        """:returns: Eight direction (north, north east, east, south east, south, south west, west, north west)"""
        return [Vector2D(*direction) for direction in cls.CARDINALS.values()]


class Vector2D(Vector, metaclass=MetaVector2D):
    NR_DIMS = 2

    def __init__(self, x: int | float, y: int | float) -> "Vector2D":
        super().__init__(x, y)
        self.x = self.dims[0]
        self.y = self.dims[1]

    def rotate90(self, clockwise: bool = True) -> "Vector2D":
        """
        Turn the Vector2D +/- 90 degrees around the Z axis.

        :param clockwise: Whether to turn clockwise. [True]
        :returns: Rotated Vector2D
        """
        if clockwise: x, y = self.y, -self.x
        else: x, y = -self.y, self.x
        return Vector2D(x, y)


class Matrix2D(Vector2D):
    """ Alias of the Vector2D class. """
    def __init__(self, x: int | float, y: int | float) -> "Matrix2D":
        super().__init__(x, y)


class Vector3D(Vector):
    NR_DIMS = 3

    def __init__(self, x: int | float, y: int | float, z: int | float):

        super().__init__(x, y, z)
        self.x = self.dims[0]
        self.y = self.dims[1]
        self.z = self.dims[2]


class Matrix3D(Vector3D):
    """ Alias of the Vector3D class. """
    def __init__(self, x: int | float, y: int | float, z: int | float) -> "Matrix3D":
        super().__init__(x, y, z)
