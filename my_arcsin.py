#!/usr/bin/env python3  # указывает Unix-подобным системам, какой интерпретатор использовать
"""
My arcsin
"""
# -*- coding: utf-8 -*-  # исполизуется кодировка UTF-8

import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 20

def my_arccsin(x):
    """
    Вычисление арксинуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = x
    multiplier = 1
    partial_sum = x
    for n in range(1, ITERATIONS):
        x_pow *= x**2  # В цикле постепенно считаем степень
        multiplier *= 2*n / (n**2 * 4)   # (2n) факториал (в числителе), (n^2) факториал и 4^n (в знаменателе)
        partial_sum += x_pow * multiplier / (2*n + 1)  # (2n + 1) в знаменателе
    return partial_sum

va = np.vectorize(my_arccsin)
print(my_arccsin, va)

vals = np.r_[-1:1:0.01]  # значения и шаг для которых будем строить графики
plt.plot(vals, np.arcsin(vals), linewidth=1.0, color='cyan')  # график библиотечного арксинуса
plt.plot(vals, va(vals), linewidth=1.0, color='black')  # график своего арксинуса
plt.show()  # показываем оба графика для наглядного сравнения
