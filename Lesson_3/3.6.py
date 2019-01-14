# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

size = 10
start = -100
stop = 100
a = [random.randint(start, stop) for _ in range(size)]
first = a[0]
second = stop
for i in range(1, size):
    if a[i] < first:
        first, second = a[i], first
    elif a[i] < second:
        second = a[i]

print(a)
print(first, second)
