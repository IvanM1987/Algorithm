# К уроку, который я пропустил :( Почему инсерт перебирает кучу списков, свигая добавление на 1 позицию влево каждый раз?
# Чем эта реализация плоха?
import random
size = 10
min = 0
max = 100
a = [random.randint(min, max) for _ in range(size)]
print(a)
b = int(input("Число: "))
c = int(input("Позиция: "))
a.append(b)
print(a)
a[c], a[size] = a[size], a[c]
print(a)

