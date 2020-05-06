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
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def norm(self):
        return np.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)


if __name__ == "__main__":
    a = Vector(0, 0, 0)
    print(f"{a.x, a.y, a.z}")
    b = Vector(1, 0, 0)
    c = a - b
    print(f"{c.x, c.y, c.z}")
    norm_c = c.norm()
    print(norm_c)
