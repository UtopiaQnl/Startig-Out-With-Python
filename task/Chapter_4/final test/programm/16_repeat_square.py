import turtle as t

t.speed(0)

NUM_SQUARES = 100
START_SQUARE_WIDTH = 10
OFFSET = 5

line = START_SQUARE_WIDTH
for square in range(NUM_SQUARES):
    # Отрисовка квадрата
    t.left(90)
    t.forward(line)
    t.left(90)
    t.forward(line)
    t.left(90)
    t.forward(line)
    t.left(90)
    t.forward(line)

    # Новое значение стороны квадрата
    line += OFFSET
