# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

size = 10
start = -100
stop = 100
a = [random.randint(start, stop) for _ in range(size)]
num = start
pos = 0
for i in range(size):
    if a[i] < 0:
        if a[i] > num:
            num = a[i]
            pos = i
print(a)
if num == 0:
    print("Отрицательных элементов в массиве нет")
print(f'Число {num} на позиции {pos}')
