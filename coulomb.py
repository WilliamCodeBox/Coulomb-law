""" 

F = k * Q1 * Q2 / R^2

In SI units:
  - Q1 and Q2 are in coulombs
  - R is in meters
  - F is in newtons
  - k = 1.0 / (4.0 * PI * eps0)
  
"""

import numpy as np

eps0 = 8.854 * 1.0e-12  # free space permittivity
k = 1.0 / (4.0 * np.pi * eps0)


def forceBtwnTwoCharges(q1, q2, dis):
    return k * q1 * q2 / np.pow(dis, 2)


def chargeByGivenForce(q, dis, force):
    return force * np.pow(dis, 2) / (k * q)


def distanceBtwnTwoCharges(q1, q2, forece):
    return np.sqrt(k * q1 * q2 / forece)


""" 

The positon of point charges can be represented by its position vector r = (x, y, z)

Given two position vectors of two point charges, r1, r2, the coulomb's law can be written as

F12 = Q1 * Q2 * (r2 - r1) / (4 * PI * eps0 * R^3)

where R = abs(r2 - r1)

"""


def vectorizedCoulomb(q1, v1, q2, v2):
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

from vector import Vector


def multiCharges(q, v, Q, V):
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


if __name__ == "__main__":
    q1 = 1e-3
    v1 = Vector(3, 2, -1)

    q2 = -2e-3
    v2 = Vector(-1, -1, 4)

    q = 10e-9
    v = Vector(0, 3, 1)

    res, force, uniVec = multiCharges(q, v, [q1, q2], [v1, v2])
    print(res * 1e3, force, uniVec)
