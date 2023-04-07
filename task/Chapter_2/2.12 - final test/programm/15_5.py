import turtle as t

t.speed(0)
t.hideturtle()
t.pensize(2)

t.goto(0, -25)
t.circle(25)
t.goto(0, 0)

t.forward(150)
t.write("Восток")
t.left(180)
t.forward(300)
t.write("Запад")
t.left(90)
t.goto(0, 0)
t.forward(150)
t.write("Юг")
t.left(180)
t.forward(300)
t.write("Север")

t.done()
