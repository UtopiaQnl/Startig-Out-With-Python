
def area(width, length):
    return width * length


def perimeter(width, length):
    return 2 * (width + length)


def main():
    width = float(input('Введите ширину прямоугольника: '))
    length = float(input('Введите длину прямоугольника: '))
    print('Площадь равна', area(width, length))
    print('Периметр равен', perimeter(width, length))


if __name__ == '__main__':
    main()
