# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

num = int(input('Введите целое положительное число: '))

num_on_work = num
num_result = ""

while num_on_work != "":
    digit = num_on_work % 10

    if num_result == "":
        num_result = digit
    else:
        num_result = num_result * 10 + digit

    if num_on_work < 10:
        num_on_work = ""
    else:
        num_on_work = num_on_work // 10

print(f'Результат - {num_result}')

