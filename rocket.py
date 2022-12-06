#!/usr/bin/env python3
"""
Kinda rocket
"""
# -*- coding: utf-8 -*-

import math
import numpy as np
from matplotlib import pyplot as pp

MODEL_G = 9.81
MODEL_DT = 0.001

class Body:
    def __init__(self, x, y, vx, vy):
        """
        Создать тело.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)

        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT

class Rocket(Body):
    def __init__(self, target):
        """
        Создать ракету.
        Старт с зесли
        Начальная скорость в 5 раз больше скорости цели
        """
        super().__init__(0, 0, 5 * target.vx, 5 * target.vy) # Вызовем конструктор предка

    def target_pos(self, target):
        """
        Получаем координаты цели
        """
        (self.target_x, self.target_y) = (target.x, target.y)

    def advance(self, target):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        Скорость меняется по модулю только из-за g
        Направление скорости - к цели
        """
        self.target_pos(target)
        self.vy -= MODEL_G * MODEL_DT

        dist = math.sqrt( (self.x - self.target_x)**2 + (self.y - self.target_y)**2)
        mod_v = math.sqrt( (self.vx)**2 + (self.vy)**2 )  # Модуль скорости и расст. до цели

        self.vx = mod_v * ( - self.x + self.target_x ) / dist  # Поворот в сторону цели
        self.vy = mod_v * ( - self.y + self.target_y ) / dist
        
        super().advance()

class Plane(Body):
    def __init__(self, x, y):
        """
        Создать самолет.
        """
        super().__init__(x, y, 75, 1) # Вызовем конструктор предка — тела, он актуален

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.vy -= MODEL_G /4 * MODEL_DT  # медлеенно снижается
        super().advance()

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
