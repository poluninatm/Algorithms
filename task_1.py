# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти..
#
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
import platform
import sys

memory_size = 0


def add_to_memory_size(var):
    global memory_size

    if isinstance(var, dict):
        memory_size += sys.getsizeof(var)
        for i in var:
            memory_size += sys.getsizeof(i)
    elif isinstance(var, list):  # только для приема списка переменных, в фукнциях не используется
        for i in var:
            add_to_memory_size(i)
    else:
        memory_size += sys.getsizeof(var)


# *********


RANGE_START = 2


# Способ 1. Перебор
def func1(range_stop):
    nums_data = dict()
    for i in range(2, 10):
        nums_data[i] = 0

    for num in range(RANGE_START, range_stop + 1):
        for i in nums_data.keys():
            if num % i == 0:
                nums_data[i] += 1

    add_to_memory_size([RANGE_START, range_stop, nums_data, nums_data.keys(), i, num])

    return nums_data


# Способ 2. Целочисленное деление
def func2(range_stop):
    nums_data = dict()
    for i in range(2, 10):
        nums_data[i] = range_stop // i

    add_to_memory_size([range_stop, nums_data, i])

    return nums_data


# Способ 3. Пройти диапазон для каждого числа 2-9
def func3(range_stop):
    nums_data = dict()
    for i in range(2, 10):
        nn = 0
        for num in range(RANGE_START, range_stop + 1):
            if num % i == 0:
                nn += 1
        nums_data[i] = nn

    add_to_memory_size([RANGE_START, range_stop, nums_data, i, nn, num])

    return nums_data


# print(func1(99))  # Память: 752
# print(func2(99))  #  Память: 648
# print(func3(99)) #  Память: 732

# print(func1(999999))  # Память: 752
# print(func2(999999))  #  Память: 648
# print(func3(999999)) #  Память: 732

# print(sys.version) # 3.7.0
# print(platform.architecture()) # ('64bit', '')

print(f'Память: {memory_size}')

# Вывод
# Отдельно на каждую функцию можно посчитать - 136 байт, но тк функции использованы для
# оформления решения и к алгоритму отношения не имеют в общую сумму их не включаю
#
# Память не растет при переборе тк использована range, которая генерирует не список а итерируемый объект,
# Все перечисленные алгоритмы не потребляют значительного количества памяти
# и использование памяти не увеличивается при увеличении рассматриваемого интервала
