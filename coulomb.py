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
