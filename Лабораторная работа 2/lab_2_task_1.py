money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

cnt = 0 # Счетчик месяцев
percent = increase + 1 # Коэффициент увеличения трат
balance = money_capital + salary # Ежемесячный бюджет

while balance >= spend:
    spend *= percent
    balance += salary - spend
    cnt += 1

print("Количество месяцев, которое можно протянуть без долгов:", cnt)
