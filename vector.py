import numpy as np


class Vector(object):
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        self._z = z

    def __sub__(self, other):
        """ Point vectors subtraction gives the distance vector """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, a):
        return Vector(self.x * a, self.y * a, self.z * a)

    def __rmul__(self, a):
        return Vector(a * self.x, a * self.y, a * self.z)

    def __truediv__(self, a):
        return Vector(self.x / a, self.y / a, self.z / a)

    def norm(self):
        return np.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __str__(self):
        return f"{self.x, self.y, self.z}"


if __name__ == "__main__":
    a = Vector(0, 0, 0)
    print(a)
    a = a * 3
    print(a)
    a = 3 * a
    print(a)
    b = Vector(1, 0, 0)
    c = a - b
    print(c)
    dis = c.norm()
    print(dis)

    unit = c / dis
    print(unit)
