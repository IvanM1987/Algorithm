# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#  Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
#  медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
#  сложно, то используйте метод сортировки, который не рассматривался на уроках
import random


def del_max(array):
    local_max = 0
    for i in range(len(array)-1):
        if array[local_max] < array[i+1]:
            local_max = i + 1
    if local_max != len(array)-1:
        array[local_max], array[len(array) - 1] = array[len(array) - 1], array[local_max]
        num = array.pop()
    else:
        num = array.pop()
    return num


array_length = 2* random.randint(1,5) + 1
array = [random.randint(0, 100) for i in range(array_length)]
print(array)
median = len(array)//2


for i in range(median):
    del_max(array)


num = del_max(array)
print(num)