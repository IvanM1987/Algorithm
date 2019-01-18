# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

size = 10
start = 0
stop = 100
a = [random.randint(start, stop) for _ in range(size)]
min_num = 100
min_num_index = 0
max_num = 0
max_num_index = 0
for i in range(size):
    if a[i] > max_num:
        max_num = a[i]
        max_num_index = i
    if a[i] < min_num:
        min_num = a[i]
        min_num_index = i
print(a)
a[max_num_index], a[min_num_index] = a[min_num_index], a[max_num_index]
print(a)
