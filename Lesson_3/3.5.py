# 5.6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.
import random

size = 10
start = 0
stop = 100
a = [random.randint(start, stop) for _ in range(size)]
min_num = 100
min_num_index = 0
max_num = 0
max_num_index = 0
plus = 0
for i in range(size):
    if a[i] > max_num:
        max_num = a[i]
        max_num_index = i
    if a[i] < min_num:
        min_num = a[i]
        min_num_index = i
if min_num_index < max_num_index:
    for x in range(min_num_index + 1, max_num_index):
        plus = plus + a[x]
else:
    for x in range(max_num_index + 1, min_num_index):
        plus = plus + a[x]
print(a)
print(f'Сумму элементов, находящихся между минимальным и максимальным элементами: {plus}')
