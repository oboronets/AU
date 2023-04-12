#!/usr/bin/env python3
"""
Monte Carlo method for Weierstrass function
"""
import math
import random
import timeit
A = 3  # график в википедии...
B = 0.5  # 2**(-50) достаточно мало

ITERS = 1_000_000
def monte_carlo_wei():
    low_l = 0
    low_b = 0
    for _ in range(ITERS):
        x = random.uniform(-1, 1)  # функция "симметрична" и должен быть ноль
        y = random.uniform(-2, 2)
        wei = sum(B**n * math.cos(A**n * math.pi * x) for n in range(0, 51))
        if (y <= wei) * (wei > 0) * (y >= 0):
            low_b += 1
        elif (y >= wei) * (y <= 0) * (wei <=0):
            low_l += 1
    approx = 4*2 * (low_b -low_l) / ITERS  # разность получается из линейности интеграла
    return approx

print(monte_carlo_wei())
# print(timeit.timeit(monte_carlo_wei, number=1))  # ~13.172
