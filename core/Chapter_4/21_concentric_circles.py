# Концентричекие круги.
import turtle as t

# Именованные константы.
NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0

# Настроить черепаху.
t.speed(ANIMATION_SPEED)
t.hideturtle()

# Задать радиус первого круга.
radius = STARTING_RADIUS

# Нарисовать круги.
for count in range(NUM_CIRCLES):
    # Нарисовать круг.
    t.circle(radius)

    # Получить координаты следующего круга.
    x = t.xcor()
    y = t.ycor() - OFFSET

    # Вычислить радиус следующего круга.
    radius = radius + OFFSET

    # Позиция черепахи для следующего круга.
    t.penup()
    t.goto(x, y)
    t.pendown()
