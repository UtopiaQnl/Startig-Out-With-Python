import matplotlib.pyplot as plt


def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords, y_coords)

    plt.title("Образец данных")

    plt.xlabel("тут иксы")
    plt.ylabel("тут игрики")

    plt.xlim(left=-1, right=10)
    plt.ylim(-1, 6)

    plt.grid(visible=True)

    plt.show()


if __name__ == "__main__":
    main()
