import turtle as t


def square(x, y, width, color):  # noqa: ANN201, D103, D103
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for _count in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()


def line(startX, startY, endX, endY, color):
    t.penup()
    t.goto(startX, startY)
    t.pendown()
    t.pencolor(color)
    t.goto(endX, endY)


def circle(x, y, radius, color):  # noqa: ANN201, D103, D103
    t.penup()
    t.goto(x, y - radius)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
