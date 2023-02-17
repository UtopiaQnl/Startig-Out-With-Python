count_Female = int(input("Введите кол-во учащихся женсокго пола: "))
count_Male = int(input("Введите кол-во учащихся мужского пола: "))

total_people = count_Female + count_Male  # Общее кол-во учащихся

procent_female = count_Female / total_people
procent_male = count_Male / total_people

print(f"Процент юношей: {procent_female:.2%}")
print(f"Процент девушек: {procent_male:.2%}")

