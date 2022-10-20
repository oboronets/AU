#!/usr/bin/env python3
"""
graf
"""
# -*- coding: utf-8 -*-


import math  # подключение пакета math
import numpy  # подключение пакета numpy
import matplotlib.pyplot as mpp  # подключение пакета Matplotlib, переименованного в mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__ == '__main__':  # если файл запущен напрямую (не как подключенный модуль):
    arguments = numpy.arange(0, 200, 0.1)  # генерирует массив чисел [0, 200) с шагом 0.1
    mpp.plot(  # строет график для x в [0, 200)...
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  # ...функции f = sin(x) * sin(x/20)
    )
    mpp.show()  # выводит этот график на экран
