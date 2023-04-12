#!/usr/bin/env python3
"""
Monte Carlo method for Weierstrass function, delta ~ 0,01
"""
import math
import random
import timeit
from multiprocessing import Pool

A = 3  # график в википедии...
B = 0.5  # 2**(-30) достаточно мало - сумма отброшенных членов ряда <= B^29
ITERS = 1_000_000

def count_b(_):  # совсем без аргументов не хочет
    """
    Считаем точки под графиком > 0
    """
    low = 0
    x = random.uniform(-1, 1)
    y = random.uniform(0, 2)
    wei = sum(B**n * math.cos(A**n * math.pi * x) for n in range(0, 31))
    if (y <= wei) * (wei > 0):
        low += 1
    return low

def count_l(_):
    """
    Считаем точки над графиком <= 0
    """
    low = 0
    x = random.uniform(-1, 1)
    y = random.uniform(-2, 0)
    wei = sum(B**n * math.cos(A**n * math.pi * x) for n in range(0, 31))
    if (y >= wei) * (wei < 0):
        low += 1
    return low

def monte_carlo_wei():
    iterable = [()]*ITERS  # вариант 1
    # iterable = list(range(ITERS))  # вариант 2
    with Pool() as pool:
        low_l = sum(pool.map(count_l, iterable))
        low_b = sum(pool.map(count_b, iterable))
    approx = 4*2 * (low_b - low_l) / ITERS  # разность получается из линейности интеграла
    print(approx)
    return approx

print(timeit.timeit(monte_carlo_wei, number=10) / 10)
#Result: 13.172  -->  2.988 (вариант 2)  -->  2.937 (вариант 1)
