salary = 5000   # Ежемесячная зарплата
spend = 6000    # Траты за первый месяц
months = 10     # Сколько месяцев нужно протянуть
increase = 0.03 # Рост цен 3%

money_capital = 0

for month in range(months):
    if spend > salary:
        money_capital += spend - salary

    spend = spend * (1 + increase)


money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
