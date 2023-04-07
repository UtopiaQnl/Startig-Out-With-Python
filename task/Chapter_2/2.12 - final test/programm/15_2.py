import turtle as t

SIDE = 230

t.speed(0)
t.pensize(3)

t.forward(SIDE)
t.left(180 - 60)
t.forward(SIDE)
t.left(180 - 60)
t.forward(SIDE)
t.left(180 - 15)

t.begin_fill()
t.forward((SIDE ** 2 / 2) ** 0.5)
t.right(90)
t.forward((SIDE ** 2 / 2) ** 0.5)
t.end_fill()

t.done()
