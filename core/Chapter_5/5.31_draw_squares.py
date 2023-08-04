import turtle as t


def main():
    t.hideturtle()
    square(100, 0, 50, "red")
    square(-150, -100, 200, "blue")
    square(-200, 150, 75, "green")


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



main()
