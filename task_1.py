# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
#
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
import cProfile

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

    return nums_data


# 100 loops, best of 5: 53.6 usec per loop - 99
# 100 loops, best of 5: 551 usec per loop - 999
# 100 loops, best of 5: 5.75 msec per loop - 9999

# cProfile.run('func1(99)')
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:7(func1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        98    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}

# cProfile.run('func1(999)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task_1.py:7(func1)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       998    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}

# print(func1(99))

# Способ 2. Целочисленное деление
def func2(range_stop):
    nums_data = dict()
    for i in range(2, 10):
        nums_data[i] = range_stop // i

    return nums_data


# 100 loops, best of 5: 901 nsec per loop - 99
# 100 loops, best of 5: 950 nsec per loop - 999
# 100 loops, best of 5: 965 nsec per loop - 9999
# 100 loops, best of 5: 966 nsec per loop - 99999

# cProfile.run('func2(99)')
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:45(func2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('func2(999)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:45(func2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Способ 3. Пройти диапазон для каждого числа 2-9
def func3(range_stop):
    nums_data = dict()
    for i in range(2, 10):
        nn = 0
        for num in range(RANGE_START, range_stop + 1):
            if num % i == 0:
                nn += 1
        nums_data[i] = nn

    return nums_data

#100 loops, best of 5: 34.8 usec per loop - 99
#100 loops, best of 5: 397 usec per loop - 999
#100 loops, best of 5: 4.27 msec per loop - 9999

# cProfile.run('func3(99)')
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:77(func3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# print(func1(99))
# print(func2(99))
# print(func3(99))


# Вывод
# Ранее задача была решена самым ресурсоемким способом. Способ 3 быстрее способа 1 за счет отсутствия обращения к ключам словаря.
# Самый быстрый способ - Способ 2.

