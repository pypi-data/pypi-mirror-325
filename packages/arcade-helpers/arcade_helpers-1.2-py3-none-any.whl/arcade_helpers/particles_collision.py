# Copyright 2023-2025 Facundo Batista
# Licensed under the Apache v2 License
# For further info, check https://github.com/facundobatista/arcade-helpers

import numpy as np


def collide(sprite1, sprite2):
    """Collide two sprites using collision dynamics.

    Linear and angular velocities will be adjusted for both sprites.

    This implements the equation 3.16 from book "Computational Granular Dynamics" by Thorsten
    Pöschel and Thomas Schwager (Springer, 2004) with the following simplifications: R=1, J̃=1.
    """
    # coefficients of restitution in normal and tangential direction
    EPS_T = -0.8  # -1 <= EPS_T <= 1
    EPS_N = 1  # 0 <= EPS_N <= 1

    # original linear velocities
    vi = np.array([sprite1.change_x, sprite1.change_y, 0])
    vj = np.array([sprite2.change_x, sprite2.change_y, 0])

    # original angular velocities
    wi = np.array([0, 0, sprite1.change_angle])
    wj = np.array([0, 0, sprite2.change_angle])

    # the unit vector pointing from sprite 2 to sprite 1
    vector = np.array([
        sprite1.center_x - sprite2.center_x,
        sprite1.center_y - sprite2.center_y,
        0,
    ])
    eij_n = vector / np.linalg.norm(vector)

    # relative velocity of colliding sprites at the point of contact, and
    # its normal and tangential projections
    g_ij = (vi - np.cross(wi, eij_n)) - (vj + np.cross(wj, eij_n))
    gij_n = (g_ij @ eij_n) * eij_n
    assert np.allclose(np.cross(eij_n, gij_n), [0, 0, 0])
    gij_t = np.cross(-eij_n, np.cross(eij_n, g_ij))

    # new linear velocities
    new_vi = vi - (1 + EPS_N) * gij_n / 2 + (EPS_T - 1) * gij_t / 4
    new_vj = vj + (1 + EPS_N) * gij_n / 2 - (EPS_T - 1) * gij_t / 4

    # new angular velocities
    delta_w = ((EPS_T - 1) / 4) * np.cross(eij_n, gij_t)
    new_wi = wi + delta_w
    new_wj = wj + delta_w

    # check resulting linear velocities have no Z component and angular velocity vector is only Z
    assert new_vi[2] == new_vj[2] == 0
    assert new_wi[0] == new_wj[0] == new_wi[1] == new_wj[1] == 0

    # convert vectors into sprite values
    sprite1.change_x, sprite1.change_y, _ = new_vi
    sprite2.change_x, sprite2.change_y, _ = new_vj
    sprite1.change_angle = new_wi[2]
    sprite2.change_angle = new_wj[2]
