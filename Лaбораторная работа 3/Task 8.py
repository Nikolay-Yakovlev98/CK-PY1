money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital > spend:
    ubitki = spend - salary
    spend = spend * 1.05
    money_capital = money_capital - ubitki
    month += 1

# TODO Оформить решение

print(month)
