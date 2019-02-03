# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

LEFT_EDGE = 0
RIGHT_EDGE = 50
SIZE = 11


def get_rand_val(left, right):
    rand = random.uniform(left, right)
    while rand == right:
        rand = random.uniform(left, right)
    return rand


def sort_merge(array):
    if len(array) <= 1:
        return

    middle = len(array) // 2
    array_1 = array[0:middle]
    array_2 = array[middle:]

    sort_merge(array_1)
    sort_merge(array_2)

    i = 0
    a1 = 0
    a2 = 0

    while len(array_1) > a1 and len(array_2) > a2:
        if array_1[a1] < array_2[a2]:
            array[i] = array_1[a1]
            a1 += 1
        else:
            array[i] = array_2[a2]
            a2 += 1

        i += 1

    while len(array_1) > a1:
        array[i] = array_1[a1]
        a1 += 1
        i += 1
    while len(array_2) > a2:
        array[i] = array_2[a2]
        a2 += 1
        i += 1


array_rand = [get_rand_val(LEFT_EDGE, RIGHT_EDGE) for _ in range(SIZE)]
array_sort = array_rand[:]
sort_merge(array_sort)

print(array_rand)
print(array_sort)
