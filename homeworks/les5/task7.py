"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
from os import path
path = path.join(path.dirname(__file__), 'task7.txt')
dict_firm = {}
dict_profit = {}
my_list = []
with open(path, 'r', encoding='utf-8') as file:
    for line in file:
        base = line.split()
        dict_firm[base[0]] = int(base[2]) - int(base[3])
    result_profit = [el for el in dict_firm.values() if el > 0]
    average_profit = sum(result_profit)/len(result_profit)
    dict_profit = {'average_profit': average_profit}
    my_list.append(dict_firm)
    my_list.append(dict_profit)
with open('task7.json', 'w') as file:
    json.dump(my_list, file)
