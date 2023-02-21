# Ввод двух цветов от пользователя.
color_one = input("Введите первый цвет: ")
color_two = input("Введите второй цвет: ")

if not (color_one == 'красный' or color_one == 'синий' or color_one == 'желтый' or \
        color_two == 'красный' or color_two == 'синий' or color_two == 'желтый'):
    print("Ошибка! Вы ввели не корректный цвет!")
else:
    if color_one == color_two:
        print(color_one)
    elif (color_one == 'красный' or color_one == 'синий') and (color_two == 'красный' or color_two == 'синий'):
        print("фиолетовый")
    elif (color_one == 'красный' or color_one == 'желтый') and (color_two == 'красный' or color_two == 'желтый'):
        print("оранжевый")
    elif (color_one == 'желтый' or color_one == 'синий') and (color_two == 'желтый' or color_two == 'синий'):
        print("зеленый")
