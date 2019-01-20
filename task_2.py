# 2. Написать два алгоритма нахождения i-го по счёту простого числа.


import cProfile

# Без использования «Решета Эратосфена»;

def func1(n):
    snums = [2]
    last_num = 3
    while len(snums) < n:
        for snum in snums:
            if last_num % snum == 0:
                break
        else:
            snums.append(last_num)

        last_num += 1
    return snums[len(snums) - 1]


# 100 loops, best of 5: 6.7 usec per loop - 10
# 100 loops, best of 5: 19.1 usec per loop - 20
# 100 loops, best of 5: 273 usec per loop - 100

# cProfile.run('func1(10)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:7(func1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        29    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('func1(1000)')
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.027    0.027 <string>:1(<module>)
#         1    0.026    0.026    0.027    0.027 task_2.py:7(func1)
#         1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#      7919    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# print(func1(10))

# Используя алгоритм «Решето Эратосфена»

def func2(n):
    pi_func = {
        4: 10,
        25: 10 ** 2,
        168: 10 ** 3,
        1229: 10 ** 4,
        9592: 10 ** 5,
        78498: 10 ** 6,
        664579: 10 ** 7,
        5761455: 10 ** 8
    }

    for num in pi_func.keys():
        if n <= num:
            size = pi_func[num]
            break
    else:
        return 'Ошибка! Сликом большое число'

    a = [0] * size
    for i in range(size):
        a[i] = i

    a[1] = 0

    m = 2
    nnum = 0
    while m < size:
        if a[m] != 0:

            nnum += 1
            if nnum == n:
                return m

            j = m * 2
            while j < size:
                a[j] = 0
                j = j + m

        m += 1

    # 100 loops, best of 5: 13.4 usec per loop - 10
    # 100 loops, best of 5: 17.4 usec per loop - 20
    # 100 loops, best of 5: 204 usec per loop - 100


# cProfile.run('func2(10)')
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:49(func2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}


# cProfile.run('func2(1000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 task_2.py:49(func2)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}


#Вывод:
#1. Использование решета Эратосфена более долгий метод на маленьких значениях n, но существенно более выигрышний с ростом n
#2. Функцию func1 можно облегчить за счет отказа от использования метода len - хранить длину в отдельной переменной,
#       но в целом это сильно скажется на производительности алгоритма

# print(func1(1000))
# print(func2(1000))
