import matplotlib.pyplot as plt


def main():
    x_coords = [0, 1, 2, 3, 5]
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords, y_coords)

    plt.title("Образце данных")

    plt.xlabel("Это ось Абсцисс")
    plt.ylabel("Это ось Ординат")

    plt.grid(visible=True)

    plt.show()


if __name__ == "__main__":
    main()
