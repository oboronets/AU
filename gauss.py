#!/usr/bin/env python3
"""
Gauss method
"""
# -*- coding: utf-8 -*-
import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def gauss(a, b):
    """ gauss method """
    a = a.copy()
    b = b.copy()
    #mb if len(a) == len(a[0])
    def forward():
        for j in range(0, len(a) - 1):
            for i in range(1, len(a) - j):
                mult = a[j+i][j] / a[j][j]
                a[j + i] -= mult *a[j]
                b[j+i] -= mult *b[j]

    def backward():
        x = numpy.zeros(len(b), dtype = float)
        for i in range(len(a[0])-1, -1, -1):
            #count summ
            summ = 0
            for j in range(i+1, len(a[0])):
                summ += x[j]*a[i][j]
            x[i] = (b[i]- summ)/a[i][i]
        return x

    forward()
    x = backward()
    return x

given_array = array([
    [1.5, 2.0, 1.5, 2],
    [3.0, 2.0, 4.0, 1],
    [1.0, 6.0, 0.0, 4],
    [2.0, 1.0, 4.0, 3]
], dtype = float)

given_values = array([5, 6, 7, 8], dtype = float)

oob_solution = solve_out_of_the_box(given_array, given_values)
solution = gauss(given_array, given_values)

print(solution)
print("Макс отклонение компоненты решения: ", norm(solution - oob_solution, ord =1))
