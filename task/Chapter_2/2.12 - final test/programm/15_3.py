import turtle as t

t.speed(0)
t.hideturtle()
t.pensize(2)

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.goto(-100, 100)
t.right(45)
t.forward((200 ** 2 * 2) ** 0.5)

t.goto(100, 0)
t.left(180)
t.forward((100 ** 2 * 2) ** 0.5)

t.penup()
t.goto(0, -100)
t.pendown()

t.forward((100 ** 2 * 2) ** 0.5)

t.done()
