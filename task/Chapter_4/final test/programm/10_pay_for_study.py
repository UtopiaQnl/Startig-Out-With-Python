COST_SEMESTER = 145e3
PROCENT_COST_UP = 0.03
DISTANCE_YEARS = 5


total_cost_for_study = 0

for year in range(DISTANCE_YEARS):
    cost_year = COST_SEMESTER * 2
    total_cost_for_study += cost_year

    print(f"Стоимость за {year} год равна - {cost_year:,.2f}р")

    COST_SEMESTER *= (1 + PROCENT_COST_UP)

print(f"Общая стоимость обучения на {DISTANCE_YEARS} лет, составляет - {total_cost_for_study:,.2f}р")

