# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

LEFT_EDGE = -100
RIGHT_EDGE = 100
SIZE = 20


def sort_bubble(array):
    for ii in range(0, len(array) - 1):
        for i in range(0, len(array) - ii - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        # print(array)


array_rand = [random.randrange(LEFT_EDGE, RIGHT_EDGE) for _ in range(SIZE)]
array_sort = array_rand.copy()
sort_bubble(array_sort)

# print('*' * 10)
print(array_rand)
print(array_sort)
