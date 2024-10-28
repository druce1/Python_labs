salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # Финансовая подушка

percent = 1 + increase # Коэффициент увеличения трат

for i in range(1, months+1):
    money_capital += spend - salary
    spend *= percent

if money_capital % 1 == 0:
    result = money_capital
else:
    result = int(money_capital) + 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", result)
