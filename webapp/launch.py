#!/usr/bin/env python3
"""
Kinda rocket, using modules
"""
import math  # import in subsubpackage's __init__ doesn't take place
import numpy as np
from matplotlib import pyplot as pp

from rocket_qt.plane import Plane
from rocket_qt.rocket import Rocket
from rocket_qt.collision import collision

class Launch():
      # constants of subsubpackage's __init__ ignored too
    #self.MODEL_G = 9.81
    def __init__(self, plane_vx, plane_vy, max_time, rocket_v):
        self.MODEL_DT = 0.001
        self.target_vx = plane_vx
        self.target_vy = plane_vy
        self.start_v = rocket_v
        self.time = max_time

    def launch_rocket(self):
        plane = Plane(self.target_vx, self.target_vy)
        rocket = Rocket(plane, self.start_v)
        podlet, bodies = collision(plane, rocket, self.time)
        self.show_graph(bodies)

        return podlet

    def show_graph(self, bodies):
        for b in bodies:
            pp.plot(b.trajectory_x, b.trajectory_y)
        pp.savefig("static/img/graf.jpg")
        pp.clf()
