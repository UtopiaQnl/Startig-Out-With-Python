# Эта программа рисует узор, используя повторяющиеся линии.
import turtle as t

# Именованные константы
START_X = -200
START_Y = 0
NUM_LINES = 36
LINE_LENGTH = 400
ANGLE = 170
ANIMATION_SPEED = 0

# Переместить черепаху в начальную позицию.
t.hideturtle()
t.penup()
t.goto(START_X, START_Y)
t.pendown()

# Задать скорость анимации.
t.speed(ANIMATION_SPEED)

# Нарисовать 36 кругов, наклоняя черепаху на
# 170 градусов после того, как каждая линия была нарисована.
for x in range(NUM_LINES):
    t.forward(LINE_LENGTH)
    t.left(ANGLE)
