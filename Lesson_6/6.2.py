# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа
import random

size = 10
start = 0
stop = 100
a = [random.randint(start, stop) for _ in range(size)]
b = []
print(a)
for i in range(size):
    if a[i] % 2 == 0:
        b.append(i)
print(b)
print('*' * 50)
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
#  уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

from collections import deque
import sys
variables = deque(globals())
for i in range(10):
    variables.popleft()
variables.remove('deque')
variables.remove('sys')
print('Переменные: ', *variables)
used_memory = 0
for i in range(len(variables)):
    used_memory += used_memory + sys.getsizeof(i)
print('Использовано памяти: ', used_memory)

