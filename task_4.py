# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array, end="\n\n")

nums = dict()

for item in array:
    if item in nums.keys():
        nums[item] += 1
    else:
        nums[item] = 1

max = dict(num=0, count=0)

for num in nums.keys():
    if(nums[num]>=max["count"]):
        max["count"]=nums[num]
        max["num"] = num

print(f'Число {max["num"]} встречается чаще всего -  {max["count"]} раз')
