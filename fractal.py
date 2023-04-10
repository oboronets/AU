#!/usr/bin/env python3
"""
Making fractal using turtle
"""
# -*- coding: utf-8 -*-
import turtle as tl

SHIFT = 3  # Рисует квадраты если SHIFT = SCALE

def draw_fractal(scale):
    """
    Algorithm for turtle
    """
    if scale >= 5:
        draw_fractal(scale - 1)
        tl.left(90)
        tl.forward(2**(scale - SHIFT))
        draw_fractal(scale - 1)
        tl.right(90)
        tl.forward(2**(scale - SHIFT))
        draw_fractal(scale - 1)
        tl.right(90)
        tl.forward(2**(scale - SHIFT))
        draw_fractal(scale - 1)
        tl.right(90)
        tl.forward(2**(scale - SHIFT))
        draw_fractal(scale - 1)
        tl.left(90)
        tl.forward(2**(scale - SHIFT))
        draw_fractal(scale - 1)
        tl.left(90)
        tl.forward(2**(scale - SHIFT))
        draw_fractal(scale - 1)
        tl.left(90)
        tl.forward(2**(scale - SHIFT))
        draw_fractal(scale - 1)
        tl.right(90)
        tl.forward(2**(scale - SHIFT))
        draw_fractal(scale - 1)
    else:
        tl.forward(2**(scale - SHIFT))


SCALE = 7

tl.pensize(1)
tl.speed(0) # fastest
tl.penup()
tl.goto(0, 0)  # if SCALE > 7, move left (-600, 0)
tl.pendown()

draw_fractal(SCALE)
tl.done()
