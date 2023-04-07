# Игра "Порази цель"
import turtle as t

# Именованные константы
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

# Настроить окно
t.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Нарисовать цель
t.hideturtle()
t.speed(0)
t.penup()
t.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
t.pendown()
t.setheading(EAST)
t.forward(TARGET_WIDTH)
t.setheading(NORTH)
t.forward(TARGET_WIDTH)
t.setheading(WEST)
t.forward(TARGET_WIDTH)
t.setheading(SOUTH)
t.forward(TARGET_WIDTH)
t.penup()

# Центрировать черепаху.
t.goto(0, 0)
t.setheading(EAST)
t.showturtle()
t.speed(PROJECTILE_SPEED)

# Получить угол выстрела и силу от пользователя.
angle = float(input("Введите угол выстрела снаряда: "))
force = float(input("Введите пусковую силу (1-10): "))

# Рассчитать расстояние.
distance = force * FORCE_FACTOR

# Задать направление.
t.setheading(angle)

# Запустить снаряд.
t.pendown()
t.forward(distance)

# Снаряд поразил цель?
if (t.xcor() >= TARGET_LLEFT_X and t.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        t.ycor() >= TARGET_LLEFT_Y and t.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Цель поражена!')
else:
    print("Вы промахнулись.")
