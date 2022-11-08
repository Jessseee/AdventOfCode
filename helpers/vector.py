# A class to store and manipulate n-dimensional vectors.

class Vector:
    """ A class to represent an n-dimensional vector. """

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
        self.__check_length(other)
        dims = (self[i] + other[i] for i in range(len(self)))
        return self.__class__(*dims)

    def __sub__(self, other):
        self.__check_length(other)
        dims = (self[i] - other[i] for i in range(len(self)))
        return self.__class__(*dims)

    def __repr__(self):
        return f"<{', '.join(map(str, self))}>"

    def __hash__(self):
        return self.dims.__hash__()

    def __eq__(self, other: "Vector") -> bool:
        self.__check_length(other)
        return self == other

    def __check_length(self, other: "Vector") -> None:
        """ Check if the length of another Vector is equal to this Vector. """
        if len(self) != len(other):
            raise ValueError("Trying to do an operation on vectors of different sizes.")


class Vector2D(Vector):
    def __init__(self, x: int | float, y: int | float) -> "Vector2D":
        super().__init__(x, y)
        self.x = self.dims[0]
        self.y = self.dims[1]

    def rotate90(self, clockwise: bool = True):
        """
        Turn the Vector2D +/- 90 degrees around the Z axis.

        :param clockwise: Whether to turn clockwise. [True]
        """
        if clockwise: self.x, self.y = self.y, -self.x
        else: self.x, self.y = -self.y, self.x


class Vector3D(Vector):
    def __init__(self, x: int | float, y: int | float, z: int | float):

        super().__init__(x, y, z)
        self.x = self.dims[0]
        self.y = self.dims[1]
        self.z = self.dims[2]
