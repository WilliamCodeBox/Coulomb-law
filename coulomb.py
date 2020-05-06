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
    return force, (v2 - v1) / dis