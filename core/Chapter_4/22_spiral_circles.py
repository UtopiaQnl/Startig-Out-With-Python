# Эта программа рисует узор, используя повторяющиесы круги.
import turtle as t

# Именованные константы.
NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATION_SPEED = 0

# Задать скорость анимации.
t.speed(ANIMATION_SPEED)

# Нарисовать 36 кругов, наклоняя черепаху на
# 10 градусов после того, как каждый круг был нарисован.
for x in range(NUM_CIRCLES):
    t.circle(RADIUS)
    t.left(ANGLE)
