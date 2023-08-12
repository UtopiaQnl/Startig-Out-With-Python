import matplotlib.pyplot as plt


def main():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]

    bar_width = 10

    plt.bar(left_edges, heights, bar_width, color=("y", "k", "g", "m", "r"))

    plt.title("Продажи c разбивкой по годам")

    plt.xlabel("Год")
    plt.ylabel("Объем продаж")

    plt.xticks((5, 15, 25, 35, 45), ("2016", "2017", "2018", "2019", "2020"))
    plt.yticks((0, 100, 200, 300, 400, 500), ("$0m", "$1m", "$2m", "$3m", "$4m", "$5m"))

    plt.show()


if __name__ == "__main__":
    main()
