# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random
from collections import deque

LEFT_EDGE = 0
RIGHT_EDGE = 200


def get_median(array):
    sum_ = 0
    for num in array:
        sum_ += num

    middle = sum_ // len(array)

    deq_left = deque()
    deq_right = deque()

    # print(middle)

    for num in array:
        if num > middle:
            if len(deq_right) == 0 or deq_right[0] > num:
                deq_right.appendleft(num)
            else:
                deq_right.append(num)
        else:
            if len(deq_left) == 0 or deq_left[-1] > num:
                deq_left.appendleft(num)
            else:
                deq_left.append(num)

    # print(deq_left, deq_right)
    if len(deq_left) > len(deq_right):
        while len(deq_left) - 1 != len(deq_right):
            deq_right.appendleft(deq_left[-1])
            deq_left.pop()
            max_left_ind = 0

            for i, num in enumerate(deq_left):
                if num > deq_left[max_left_ind]:
                    max_left_ind = i

            deq_left[max_left_ind], deq_left[-1] = deq_left[-1], deq_left[max_left_ind]
            # print(deq_left, deq_right)

        return deq_left[-1]
    else:
        while len(deq_right) - 1 != len(deq_left):
            deq_left.append(deq_right[0])
            deq_right.popleft()
            min_right_ind = 0

            for i, num in enumerate(deq_right):
                if num < deq_right[min_right_ind]:
                    min_right_ind = i

            deq_right[min_right_ind], deq_right[0] = deq_right[0], deq_right[min_right_ind]
            # print(deq_left, deq_right)

        return deq_right[0]


m = int(input('Введите m: '))

array = [random.randrange(LEFT_EDGE, RIGHT_EDGE) for _ in range(2 * m + 1)]

print(array)
print(f'Медиана: {get_median(array)}')

# print(sorted(array))
