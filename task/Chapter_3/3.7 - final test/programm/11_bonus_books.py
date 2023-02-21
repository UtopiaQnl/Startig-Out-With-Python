count_book = int(input("Введите количество книг, купленных в этом месяце: "))

total_bonus = 0

if count_book >= 2:
    total_bonus += 5
elif count_book >= 4:
    total_bonus += 15
elif count_book >= 6:
    total_bonus += 30
elif ocunt >= 8:
    total_bonus += 60

print(f"За купленный книги вам положено {total_bonus} очков!")

