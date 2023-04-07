user_age = int(input("Введите свой возраст в годах: "))

print("Вы -", end=" ")

if user_age <= 1:
    print("Младенец")
elif user_age <= 13:
    print("Ребенок")
elif user_age <= 20:
    print("Подросток")
else:
    print("Взрослый")
