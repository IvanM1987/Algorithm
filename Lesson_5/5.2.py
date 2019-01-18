from collections import deque

a = deque(input("Введите первое число: "))
b = deque(input("Введите второн число: "))
c = deque(0 for i in range((len(a) * 2) if len(a) > len(b) else (len(b) * 2)))
a.extendleft('0' * (len(c) - len(a)))
b.extendleft('0' * (len(c) - len(b)))
d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
e = c.copy()
for i in range(len(a)):
    if a[i] in d:
        a[i] = d.index(a[i])
    if b[i] in d:
        b[i] = d.index(b[i])

# 1.Сложение
for i in range(len(c) - 1, -1, -1):
    c[i] += a[i] + b[i]
    if c[i] > 15:
        c[i - 1] += 1
        c[i] = d[c[i] - 16]
    else:
        c[i] = d[c[i]]

# 2.Умножение
for i in range(len(e)):
    for p in range(len(e)):
        e[p - i] += a[len(a) - i - 1] * b[p]
for i in range(len(a) - 1, -1, -1):
    if e[i] > 15:
        x = e[i] // 16
        e[i - 1] += x
        e[i] = d[e[i] % 16]
    else:
        e[i] = d[e[i]]


# Убираем лишнее из массивов с ответами. Почему-то не все нули убираются. Был бы благодарен, если бы подсказали :)
i = 0
while True:
    if c[i] == '0':
        c.popleft()
        i += 1
    else:
        break
while True:
    if e[i] == '0':
        e.popleft()
        i += 1
    else:
        break


sum_of_two = ''.join(c)
mult = ''.join(e)
print(f'Сумма равна:{sum_of_two}, произведение равно: {mult}')
