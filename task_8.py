# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
year = int(input("Введите номер года: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print('Год високосный')
        else:
            print('Год невисокосный')
    else:
        print('Год високосный')
else:
    print('Год невисокосный')