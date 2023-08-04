import turtle as t

TOP_X = 0
TOP_Y = 100
BASE_LEFT_X = -100
BASE_LEFT_Y = -100
BASE_RIGHT_X = 100
BASE_RIGHT_Y = -100


def main():
    t.hideturtle()
    line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, "red")
    line(TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGHT_Y, "blue")
    line(BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGHT_Y, "green")


def line(startX, startY, endX, endY, color):
    t.penup()
    t.goto(startX, startY)
    t.pendown()
    t.pencolor(color)
    t.goto(endX, endY)


main()
