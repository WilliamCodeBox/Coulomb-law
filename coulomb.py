""" 

F = k * Q1 * Q2 / R^2

In SI units:
  - Q1 and Q2 are in coulombs
  - R is in meters
  - F is in newtons
  - k = 1.0 / (4.0 * PI * eps0)
  
"""

import numpy as np
from vector import Vector
from typing import Union, List, Tuple

T = Union[int, float]

eps0 = 8.854 * 1.0e-12  # free space permittivity
k = 1.0 / (4.0 * np.pi * eps0)


def forceBtwnTwoCharges(q1: T, q2: T, dis: T) -> float:
    return k * q1 * q2 / np.pow(dis, 2)


def chargeByGivenForce(q: T, dis: T, force: T) -> float:
    return force * np.pow(dis, 2) / (k * q)


def distanceBtwnTwoCharges(q1: T, q2: T, forece: T) -> float:
    return np.sqrt(k * q1 * q2 / forece)


""" 

The positon of point charges can be represented by its position vector r = (x, y, z)

Given two position vectors of two point charges, r1, r2, the coulomb's law can be written as

F12 = Q1 * Q2 * (r2 - r1) / (4 * PI * eps0 * R^3)

where R = abs(r2 - r1)

"""


def vectorizedCoulomb(q1: T, v1: Vector, q2: T,
                      v2: Vector) -> Tuple[Vector, float, Vector]:
    dis = (v2 - v1).norm()
    force = q1 * q2 / (4.0 * np.pi * eps0 * np.pow(dis, 2))
    uniVec = (v2 - v1) / dis
    result = force * uniVec
    return result, force, uniVec


""" 

Principle of Superposition

The resultant force F on a charge Q located at point vector r is 
the vector sum of the forces exerted on Q by each of the charges Q1, Q2, ..., QN,

"""


def multiCharges(q: T, v: Vector, Q: List[T],
                 V: List[Vector]) -> Tuple[Vector, float, Vector]:
    N = len(Q)
    assert (N == len(V))

    factor = q / (4.0 * np.pi * eps0)

    sum = Vector(0.0, 0.0, 0.0)

    for idx in np.arange(0, N):
        dis = (v - V[idx]).norm()
        sum = sum + ((v - V[idx]) / np.power(dis, 3)) * Q[idx]
    result = sum * factor
    force = result.norm()
    uniVec = result / result.norm()
    return result, force, uniVec


""" 

Electric field intensity or Electric field strength 

is the force that a unit positive charge experiences when placed in an electric field

The electric field intensity at point r due to a point charge Q located at r0 is 

E = Q * (r - r0) / (4 * PI * eps0 * R^3)

where R = abs(r - r0)

Or simply

E = Q / (4 * PI * eps0 * R^2) * u

where u is the unit vector pointing from r0 to r

When Q is negative, E is directing from r to r0
When Q is positive, E is directing from r0 to r

we can move the sign of Q into u

"""


def ElecFieldOfPointCharge(q: T, v0: Vector,
                           v: Vector) -> Tuple[Vector, float, Vector]:
    dis = (v - v0).norm()
    intensity = np.abs(q) / (4.0 * np.pi * eps0 * np.power(dis, 2))
    uniVec = (q / np.abs(q)) * (v - v0) / dis
    Efield = intensity * uniVec

    return Efield, intensity, uniVec


def ElecFieldOfMultiCharges(Q: List[T], V: List[Vector], v):
    factor = 1.0 / (4.0 * np.pi * eps0)

    N = len(Q)
    assert (N == len(V))

    sum = Vector(0.0, 0.0, 0.0)

    for idx in np.arange(0, N):
        dis = (v - V[idx]).norm()
        sum = sum + Q[idx] * (v - V[idx]) / np.power(dis, 3)

    Efield = factor * sum
    intensity = Efield.norm()
    uniVec = Efield / intensity

    return Efield, intensity, uniVec


if __name__ == "__main__":
    q1 = 1e-3
    v1 = Vector(3, 2, -1)

    q2 = -2e-3
    v2 = Vector(-1, -1, 4)

    q = 10e-9
    v = Vector(0, 3, 1)

    res, force, uniVec = multiCharges(q, v, [q1, q2], [v1, v2])
    print(res * 1e3, force, uniVec)

    E, intensity, uniVec = ElecFieldOfMultiCharges([q1, q2], [v1, v2], v)
    print(E / 1e3)

if __name__ == "__main__":
    q1 = 5e-9
    v1 = Vector(2, 0, 4)

    q2 = -2e-9
    v2 = Vector(-3, 0, 5)

    q = 1e-9
    v = Vector(1, -3, 7)

    res, _, _ = multiCharges(q, v, [q1, q2], [v1, v2])
    print(res / 1e-9)

    E, _, _ = ElecFieldOfMultiCharges([q1, q2], [v1, v2], v)
    print(E)