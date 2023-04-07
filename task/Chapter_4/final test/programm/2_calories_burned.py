CALORIES_PER_MIN = 4.2

for minutes in range(10, 31, 5):
    calories_burned = CALORIES_PER_MIN * minutes
    print(f"Калорий сожжено после {minutes} равно - {calories_burned:,.2f}")
