#!/usr/bin/env python3
"""
Kinda rocket, using modules
"""
import math  # import in subsubpackage's __init__ doesn't take place
import numpy as np
from matplotlib import pyplot as pp

from some_physics.plane import Plane
from some_physics.rocket import Rocket

MODEL_DT = 0.001  # constants of subsubpackage's __init__ ignored too
MODEL_G = 9.81

p = Plane(0, 5000)
r = Rocket(p)

bodies = [p, r]

for t in np.arange(0, 60, MODEL_DT): # для всех временных отрезков
    p.advance()
    r.advance(p)
    if (math.fabs(p.x - r.x) < 1) * (math.fabs(p.y - r.y) < 1):  # учитваем, что тела имеют какие-то реальные размеры
        break  # после попадания ракеты advance к самолету и ракете не применить...

for b in bodies: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y) # нарисуем их траектории
pp.show()
