CUP_SUGAR = 1.5
CUP_OIL = 1
CUP_FLOUR = 2.75
COOKIES = 48

count_bun = int(input("Введите кол-во булочек, которые вы хотите испеч: "))

cup_sugar_for_user = count_bun * CUP_SUGAR / COOKIES
cup_oil_for_user = count_bun * CUP_OIL / COOKIES
cup_flour_for_user = count_bun * CUP_FLOUR / COOKIES

print(f"Для изготовления {count_bun} булочек нужно:")
print(f"  1. {cup_sugar_for_user:.2f} стакана сахара.")
print(f"  2. {cup_oil_for_user:.2f} стакана масла.")
print(f"  3. {cup_flour_for_user:.2f} стакана муки.")

