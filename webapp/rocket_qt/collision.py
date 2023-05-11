#!/usr/bin/env python3
"""
To collide
"""
import math
import numpy as np
from matplotlib import pyplot as pp

from .plane import Plane
from .rocket import Rocket

MODEL_DT = 0.001
MODEL_G = 9.81

def collision(plane, rocket, time):
    p = plane
    r = rocket
    bodies = [p, r]
    podlet = 0
    for t in np.arange(0, time, MODEL_DT): # для всех временных отрезков
        p.advance()
        r.advance(p)
        if (math.fabs(p.x - r.x) < 10) * (math.fabs(p.y - r.y) < 10):  # учитваем, что тела имеют какие-то реальные размеры
            podlet = t
            break  # после попадания ракеты advance к самолету и ракете не применить...

    return podlet, bodies
