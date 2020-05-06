import numpy as np
from typing import TypeVar, Union, NoReturn

T = Union[int, float]


class Vector(object):
    def __init__(self, x: T, y: T, z: T):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> T:
        return self._x

    @x.setter
    def x(self, x: T):
        self._x = x

    @property
    def y(self) -> T:
        return self._y

    @y.setter
    def y(self, y: T):
        self._y = y

    @property
    def z(self) -> T:
        return self._z

    @z.setter
    def z(self, z: T):
        self._z = z

    def __sub__(self, other):
        """ Point vectors subtraction gives the distance vector """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, a: T):
        return Vector(self.x * a, self.y * a, self.z * a)

    def __rmul__(self, a: T):
        return Vector(a * self.x, a * self.y, a * self.z)

    def __truediv__(self, a: T):
        return Vector(self.x / a, self.y / a, self.z / a)

    def norm(self) -> T:
        return np.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __str__(self) -> str:
        return f"{self.x, self.y, self.z}"


if __name__ == "__main__":
    a = Vector(0, 0, 0)
    print(a)
    a = a * 3
    print(a)
    b = Vector(1, 0, 0)
    c = a - b
    print(c)
    dis: T = c.norm()
    print(dis)

    unit = c / dis
    print(unit)

    print(type(unit))
