# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы
# диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

a = int(input('Введите 2 целых числа, в границах которых будет выбрано случайное.\n'
              'Введите меньшее число: '))
b = int(input('Введите большее число: '))
print(random.randint(a, b))
a = int(input('Введите 2 целых числа, в границах которых будет выбрано случайное.\n'
              'Введите меньшее число: '))
b = int(input('Введите большее число: '))
print(random.uniform(a, b))

a = ord(input('Введите 2 буквы англ. алфавита между которыми будет выбрана случайная. \n'
              'Введите букву, которая находится раньше по алфавиту: '))
b = ord(input('Вторая буква: '))
print(chr(random.randint(a, b)))
