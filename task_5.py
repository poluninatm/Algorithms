# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array, end="\n\n")

max = dict(index=None, value=None)

for i, item in enumerate(array):
    if item < 0:
        if max["value"] is None or max["value"] < item:
            max["value"] = item
            max["index"] = i

if max["value"] is None:
    print(f'В массиве нет отрицательных чисел')
else:
    print(f'Максимальное отрицательное число {max["value"]} с индексом {max["index"]}')

