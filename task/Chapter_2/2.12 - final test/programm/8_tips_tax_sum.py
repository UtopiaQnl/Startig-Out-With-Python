TIPS_TAX = 0.18
TAX_SALE = 0.07

cost_eat = float(input("Введите стоимость еды: "))

resultTip = cost_eat * TIPS_TAX
resultTax = cost_eat * TAX_SALE
resultSum = resultTip + resultTax + cost_eat

print(f"Процент {TIPS_TAX:.2%} чаевых: ${resultTip:.2f}")
print(f"Налог продажи {TAX_SALE:.2%}: ${resultTax:.2f}")
print(f"Итоговая сумма: ${resultSum:.2f}")

