# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array, end="\n\n")

max = dict(index=0, value=array[0])
min = dict(index=0, value=array[0])

for i, item in enumerate(array):

    if max["value"] <= item:
        max["value"] = item
        max["index"] = i

    if min["value"] >= item:
        min["value"] = item
        min["index"] = i

array[max["index"]] = min["value"]
array[min["index"]] = max["value"]

print(f'Максимальный элемент {max["value"]} с индексом {max["index"]}')
print(f'Минимальный элемент {min["value"]} с индексом {min["index"]}', end="\n\n")

print(array)
