def main():
    num = 3
    from_tower = 1
    to_tower = 3
    tmp_tower = 2

    move_discs(num, from_tower, to_tower, tmp_tower)
    print("DONE")


def move_discs(num, from_t, to_t, tmp_t):
    if num > 0:
        move_discs(num - 1, from_t, tmp_t, to_t)
        print("Переместили c", from_t, "на", to_t)
        move_discs(num - 1, tmp_t, to_t, from_t)


if __name__ == "__main__":
    main()
