import numpy as np


class Vector(object):
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_z(self):
        return self._z

    def set_z(self, z):
        self._z = z

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    z = property(get_z, set_z)

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
