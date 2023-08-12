import random

ROWS = 3
COSL = 4


def main():
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    for r in range(ROWS):
        for c in range(COSL):
            values[r][c] = random.randint(1, 100)

    print(values)


if __name__ == "__main__":
    main()
