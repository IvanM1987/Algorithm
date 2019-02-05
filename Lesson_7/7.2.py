# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
array = [round(random.uniform(0,49.999),3) for i in range(1,11)]
random.shuffle(array)
print(array)
def split_sort(array):
    left = []
    right = []
    final = []
    if len(array) > 1:
        half = len(array)//2
        left = array[:half]
        right = array[half:]
        split_sort(left)
        split_sort(right)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            array[k] = right[j]
            j+=1
        else:
            array[k] = left[i]
            i+=1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        array[k] = right[j]
        j+=1
        k+=1
split_sort(array)
print(array)