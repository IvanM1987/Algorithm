# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
a = [_ for _ in range(2, 100)]

dev = 2
while dev < 10:
    count = 0
    for i in range(0, 98):
        if a[i]%dev ==0:
            count +=1
            i +=1
        i+=1
    print(count)
    dev+=1
print('*' * 50)
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
#  уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

from collections import deque
import sys
variables = deque(globals())
for i in range(9):
    variables.popleft()
variables.remove('deque')
variables.remove('sys')
print('Переменные: ', *variables)
used_memory = 0
for i in range(len(variables)):
    used_memory += used_memory + sys.getsizeof(i)
print('Использовано памяти: ', used_memory)
