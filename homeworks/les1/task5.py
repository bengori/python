"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность
выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
"""

proceeds = float(input('Введите значение выручки фирмы (в у.е.):\n>>>'))
costs = float(input('Введите размер издержек фирмы (в у.е.):\n>>>'))
profit = round(proceeds - costs, 2)
loss = round(costs - proceeds, 2)
profitability = round(profit/proceeds, 2)

if proceeds > costs:
    print(f'Финансовый результат - прибыль {profit} (у.е.)')
    print(f'Рентабельность выручки {profitability}')
    number_employees = int(input('Введите количество сотрудников фирмы:\n>>>'))
    profit_employees = round(profit / number_employees, 2)
    print(f'Прибыль на одного сотрудника {profit_employees} (у.е.)')
else:
    print(f'Финансовый результат - убыток {loss} (у.е.)')