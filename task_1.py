# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = input("Введите трехзначное число: ")

num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])

summa = num1 + num2 + num3
product = num1 * num2 * num3

print(f'Сумма: {summa}. Произведение: {product}')
