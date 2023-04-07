import turtle as t

t.hideturtle()
t.speed(0)

OFFSET = 5
TURNS = 100

line = 5

for _ in range(TURNS):
    t.forward(line)
    line += OFFSET
    t.left(90)
