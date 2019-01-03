# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

RANGE_START = 2
RANGE_STOP = 99

nums_data = dict()
for i in range(2, 10):
    nums_data[i] = 0

# print(nums_data)

for num in range(RANGE_START, RANGE_STOP + 1):
    for i in nums_data.keys():
        if num % i == 0:
            nums_data[i] += 1

for i in nums_data.keys():
    print(f' {i} - кратно {nums_data[i]} чисел')
