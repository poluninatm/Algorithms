# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

array_1=[8, 3, 15, 6, 4, 2]
array_2=[]

for i, item in enumerate(array_1):
    if item % 2 == 0:
        array_2.append(i)

print(array_1)
print(array_2)
