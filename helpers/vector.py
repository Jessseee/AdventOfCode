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


class MetaVector2D(type):
    DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    DIRECTION_NAMES = {
        'north': 0, 'up': 0, 'north_east': 1, 'east': 2, 'right': 2, 'south_east': 3, 'south': 4,
        'down': 4, 'south_west': 5, 'west': 6, 'left': 6, 'north_west': 7, 'center': 8
    }

    def __getattr__(cls, key):
        index = cls.DIRECTION_NAMES.get(key)
        if index is not None:
            return lambda: Vector2D(*cls.DIRECTIONS[index])
        raise AttributeError(key)


class Matrix(Vector):
    """ Alias of the Vector class. """
    def __init__(self, *dims):
        super().__init__(*dims)


class Vector2D(Vector, metaclass=MetaVector2D):
    NR_DIMS = 2

    def __init__(self, x: int | float, y: int | float) -> "Vector2D":
        super().__init__(x, y)
        self.x = self.dims[0]
        self.y = self.dims[1]

    def rotate90(self, clockwise: bool = True):
        """
        Turn the Vector2D +/- 90 degrees around the Z axis.

        :param clockwise: Whether to turn clockwise. [True]
        """
        if clockwise: x, y = self.y, -self.x
        else: x, y = -self.y, self.x
        return Vector2D(x, y)


class Vector3D(Vector):
    NR_DIMS = 3

    def __init__(self, x: int | float, y: int | float, z: int | float):

        super().__init__(x, y, z)
        self.x = self.dims[0]
        self.y = self.dims[1]
        self.z = self.dims[2]
