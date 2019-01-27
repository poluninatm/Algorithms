# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.
from collections import namedtuple

cnt = int(input('Введите количество предприятий: '))

firms = []
Firm = namedtuple('Firm', 'name profit_1 profit_2 profit_3 profit_4 year_profit')
firmsSumProfit = 0

while len(firms) < cnt:
    name = input('Название предприятия: ')
    profit_1 = int(input('Прибыль за 1 квартал: '))
    profit_2 = int(input('Прибыль за 2 квартал: '))
    profit_3 = int(input('Прибыль за 3 квартал: '))
    profit_4 = int(input('Прибыль за 4 квартал: '))
    year_profit = profit_1 + profit_2 + profit_3 + profit_4

    print(f'Прибыль за год: {year_profit}')
    firmsSumProfit += year_profit
    firm = Firm(name=name, profit_1=profit_1, profit_2=profit_2, profit_3=profit_3, profit_4=profit_4,
                year_profit=year_profit)
    firms.append(firm)

avr = firmsSumProfit / cnt
print(f'Средняя прибыль предприятия за год: {avr}')

print('*' * 50)

firmsProfBigger = []
firmsProfSmaller = []

for firm in firms:
    if firm.year_profit <= avr:
        firmsProfBigger.append(firm)
    else:
        firmsProfSmaller.append(firm)

print('Предприятия с годовой прибылью средней и выше средней: ')
for firm in firmsProfBigger:
    print(firm.name)

print('Предприятия с годовой прибылью ниже средней: ')
for firm in firmsProfSmaller:
    print(firm.name)
