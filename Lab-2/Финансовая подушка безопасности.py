money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
mesacev = 0
bydget = money_capital + salary
while bydget > spend:
    bydget -= spend
    mesacev += 1
    spend = spend + (increase * spend)
    bydget += salary
print("Количество месяцев, которое можно протянуть без долгов:", mesacev)