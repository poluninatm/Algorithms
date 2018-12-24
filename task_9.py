# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def get_num_sum(num):
    if num < 10:
        return num
    return num % 10 + get_num_sum(num // 10)


biggest = 0
summ = 0

while True:
    num = int(input('Введите натуральное число или 0 для завершения ввода чисел: '))

    if num == 0:
        break

    num_sum = get_num_sum(num)
    if num_sum >= summ:
        biggest = num
        summ = num_sum

print(f'Число с самой большой суммой цифр - {biggest}, его сумма - {summ}')
