# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ..
# .Количество элементов (n) вводится с клавиатуры.
def sum(a,result, n):
    result = result + a
    b = -0.5
    a = a * b
    n -= 1
    if n == 0:
        return print(result)
    else:
        sum(a,result,n)
sum(1, 0, int(input("Введите кол-во итераций: ")))