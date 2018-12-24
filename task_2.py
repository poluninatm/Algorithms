# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите натуральное число: '))
odd = 0
even = 0
num_on_work = num

while num_on_work != 0:
    digit = num_on_work % 10

    if digit % 2 > 0:
        odd += 1
    else:
        even += 1

    num_on_work = num_on_work // 10


print(f'В числе {odd} нечетных и {even} четных цифр')
