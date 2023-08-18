def main():
    print("Первые 10 чисел")
    print("последовательности Фибоначчи")

    for number in range(1, 11):
        print(fib(number))


def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    main()
