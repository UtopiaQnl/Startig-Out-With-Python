# Данные при покупке
COUNT_PURCHASES = 2000
COST_PURCHASE_ONE_ACTION = 40
TAX_PURCHASES = 0.03

# Данные при продаже
COUNT_SALES = 2000
COST_SALE_ONE_ACTION = 42.75
TAX_SALES = 0.03

# Потраченные деньги на акции при покупке
spent_money_for_actions = COUNT_PURCHASES * COST_PURCHASE_ONE_ACTION
# Сумма комиссии при покупке акций
sum_tax_buy = spent_money_for_actions * TAX_PURCHASES

# Сумма продажи акций
sale_shares = COUNT_SALES * COST_SALE_ONE_ACTION
# Сумма комиссии при продаже акций
sum_tax_sale = sale_shares * TAX_SALES

# Итоговая оставшаяся сумма
result_sum = sale_shares - (sum_tax_sale + sum_tax_buy + spent_money_for_actions)

print(f"Потраченные деньги при покупке акций: ${spent_money_for_actions:,.2f}")
print(f"Сумма комисси при покупке акций: ${sum_tax_buy:,.2f}")
print(f"Сумма продажи акций: ${sale_shares:,.2f}")
print(f"Сумма комисси при продаже акций: ${sum_tax_sale:,.2f}")
print(f"Итоговая оставшаяся сумма: ${result_sum:,.2f}")

