import turtle as tl

def draw_fractal(scale):
    if scale >= 5:
        draw_fractal(scale / 3.0)
        tl.left(2)
        draw_fractal(scale / 3.0)
        tl.right(4)
        draw_fractal(scale / 3.0)
        tl.left(6)
        draw_fractal(scale / 3.0)
    else:
        tl.forward(scale)

scale = 1000
tl.pensize(2)
tl.penup()
tl.goto(-400, -100)
tl.pendown()

draw_fractal(scale)
tl.done()