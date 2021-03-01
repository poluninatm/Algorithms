# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как ['A', '2'] и ['C', '4', 'F'] соответственно.
# Сумма чисел из примера: ['C', 'F', '1'], произведение - ['7', 'C', '9', 'F', 'E'].
from collections import deque

hToN = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
        'D': 13, 'E': 14, 'F': 15}
nToH = {value: key for key, value in hToN.items()}


def summ(num1, num2):
    mem = 0
    num1, num2 = num1[:], num2[:]

    result = deque()
    while True:
        this_num = 0
        if len(num1) > 0:
            this_num = hToN[num1.pop()]

        if len(num2) > 0:
            this_num += hToN[num2.pop()]

        this_num += mem

        if this_num > 15:
            mem = this_num // 16
            this_num = this_num % 16
        else:
            mem = 0

        result.appendleft(nToH[this_num])
        if len(num1) == 0 and len(num2) == 0 and mem == 0:
            break
    return list(result)


def times(num1, num2):
    pluses = []

    for i1, n1 in enumerate(num1):
        for i2, n2 in enumerate(num2):
            this_num = deque()

            n = hToN[n1] * hToN[n2]
            if n > 15:
                this_num.append(nToH[n // 16])
                n = n % 16

            this_num.append(nToH[n])
            order = (len(num1) - 1 - i1) + (len(num2) - 1 - i2)
            if order > 0:
                this_num.extend(['0'] * order)

            pluses.append(list(this_num))

    result = []

    for plus in pluses:
        if len(result) == 0:
            result = plus
        else:
            result = summ(result, plus)

    return result


inp1 = list(input('Введите первое шестнадцатеричное число: '))
inp2 = list(input('Введите второе шестнадцатеричное число: '))

print(summ(inp1, inp2))
print(times(inp1, inp2))
