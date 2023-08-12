import matplotlib.pyplot as plt


def main():
    values = (20, 60, 80, 40)
    slice_labels = ("Assembly", "Python", "C", "Makrdown")

    plt.pie(values, labels=slice_labels)

    plt.title("Языки")

    plt.show()


if __name__ == "__main__":
    main()
