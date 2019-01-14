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

