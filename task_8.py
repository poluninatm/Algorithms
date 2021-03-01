# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def count_digit(num, digit):
    now_digit = num % 10
    if now_digit == digit:
        r = 1
    else:
        r = 0

    if num < 10:
        return r

    return r + count_digit(num // 10, digit)


cnt = int(input('Введите количество чисел: '))
digit = int(input('Введите отслеживаемую цифру: '))

digit_count = 0

while cnt > 0:
    num = int(input('Введите число: '))
    digit_count += count_digit(num, digit)
    cnt -= 1

print(f'Цифра встретилась {digit_count} раз')
