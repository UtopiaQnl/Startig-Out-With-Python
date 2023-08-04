import turtle as t

import my_graphics as mg

X1 = 0
Y1 = 100
X2 = -100
Y2 = -100
X3 = 100
Y3 = -100
RADIUS = 50


def main():
    t.hideturtle()

    mg.square(X2, Y2, (X3 - X2), "gray")

    mg.circle(X1, Y1, RADIUS, "blue")
    mg.circle(X2, Y2, RADIUS, "red")
    mg.circle(X3, Y3, RADIUS, "green")

    mg.line(X1, Y1, X2, Y2, "black")
    mg.line(X1, Y1, X3, Y3, "black")
    mg.line(X2, Y2, X3, Y3, "black")


main()
