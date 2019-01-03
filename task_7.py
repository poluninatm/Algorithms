# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array, end="\n\n")

min1 = dict(index=0, value=array[0])
min2 = dict(index=1, value=array[1])

if array[0] < array[1]:
    min1["value"] = array[1]
    min1["index"] = 1
    min2["value"] = array[0]
    min2["index"] = 0

for i, item in enumerate(array):
    if i > 1 and item <= min1["value"]:
        if item <= min2["value"]:
            min1["value"] = min2["value"]
            min1["index"] = min2["index"]

            min2["value"] = item
            min2["index"] = i
        else:
            min1["value"] = item
            min1["index"] = i

print(f'Минимальное число  {min2["value"]} с индексом {min2["index"]}')
print(f'Минимальное число  {min1["value"]} с индексом {min1["index"]}')

