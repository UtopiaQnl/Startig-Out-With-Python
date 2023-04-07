import turtle as t

RADIUS = 100
K = (RADIUS * 1/4) + RADIUS

t.speed(0)
t.hideturtle()
t.pensize(2)

t.circle(RADIUS)

t.penup()
t.goto(K * 2, 0)
t.pendown()

t.circle(RADIUS)

t.penup()
t.goto(K * 4, 0)
t.pendown()

t.circle(RADIUS)

t.penup()
t.goto(K, -RADIUS)
t.pendown()

t.circle(RADIUS)

t.penup()
t.goto(K * 3, -RADIUS)
t.pendown()

t.circle(RADIUS)

t.done()

