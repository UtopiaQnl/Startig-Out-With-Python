import turtle as t

t.hideturtle()
t.speed(0)
t.right(45)

LINE_LENGTH = 100
ANGLE = 135
COUNT_VERTEX = 8

for vertex in range(COUNT_VERTEX):
    t.right(ANGLE)
    t.forward(LINE_LENGTH)
