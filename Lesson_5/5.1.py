# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.
from collections import namedtuple

firm = namedtuple('firm', 'name, first, second, third, forth')

a = int(input('Введите количество предприятий для анализа: '))
print('Введите название предприятия на англ. и его квартальную прибыль за 4 квартала.')
firms_list = []
firm_profit = []
profit = 0

for i in range(a):
    name = input('Название: ')

    first = int(input('Прибыль за первый квартал: '))
    second = int(input('Прибыль за второй квартал: '))
    third = int(input('Прибыль за третий квартал: '))
    forth = int(input('Прибыль за четвертый квартал: '))

    name = firm(name, first, second, third, forth)
    firms_list.append(name)


for i in range(a):
    firm_sum = (firms_list[i].first + firms_list[i].second + firms_list[i].third + firms_list[i].forth)
    profit = profit + firm_sum
    firm_profit.append(firm_sum)

print(f"Средняя прибыль за год по всем фирмам: {profit/a}")
for i in range(a):
    if firm_profit[i] >= profit / a:
        print(f'Фирма {firms_list[i].name} зарабатывает выше среднего.')
    else:
        print(f'Фирма {firms_list[i].name} зарабатывает ниже среднего.')
