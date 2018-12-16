# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print('Введите три разных числа')
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))

if num1 > num2:
    b1 = num1
    b2 = num2
else:
    b1 = num2
    b2 = num1

if b2 > num3:
    middle = b2
elif b1 > num3:
    middle = num3
else:
    middle = b1

print(f'Среднее число: {middle}')