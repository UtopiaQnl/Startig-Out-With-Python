def main():
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите ещё одно число: '))

    quotient = devide(num1, num2)

    if quotient is None:
        print('Деление на ноль невозможно!')
    else:
        print(f"{num1} поделить на {num2} равняется {quotient}.")


def devide(num1, num2):
    if num2 == 0:
        result = None
    else:
        result = num1 / num2

    return result


main()
