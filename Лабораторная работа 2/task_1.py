money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0              # Счётчик месяцев

while True:
    budget = money_capital + salary
    if budget < spend:
        break

    money_capital = budget - spend

    spend = spend * (1 + increase)

    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)