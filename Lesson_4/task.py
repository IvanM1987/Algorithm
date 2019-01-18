# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


# Вариант 1
def first(n=100):
    a = [_ for _ in range(2, n)]
    b = []
    dev = 2
    while dev < 10:
        count = 0
        for i in range(len(a)):
            if a[i] % dev == 0:
                count += 1
                i += 1
            i += 1
        b.append(count)
        dev += 1
    return b


# 100 loops, best of 5: 163 usec per loop   - 100
# 100 loops, best of 5: 1.98 msec per loop  - 1000
# 100 loops, best of 5: 10.3 msec per loop  - 5000


# 100
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task.py:5(first)
#         1    0.000    0.000    0.000    0.000 task.py:6(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 1000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 task.py:5(first)
#         1    0.000    0.000    0.000    0.000 task.py:6(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#  50 000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.111    0.111 <string>:1(<module>)
#         1    0.109    0.109    0.111    0.111 task.py:5(first)
#         1    0.002    0.002    0.002    0.002 task.py:6(<listcomp>)
#         1    0.000    0.000    0.111    0.111 {built-in method builtins.exec}
#         8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 2
# Считает вплоть до n-1.

def second(n=100):
    a = []
    for i in range(2, 10):
        a.append((n - 1) // i)
    return a

# 100 loops, best of 5: 2.11 usec per loop  - 100
# 100 loops, best of 5: 2.26 usec per loop  - 1000
# 100 loops, best of 5: 2.37 usec per loop  - 5000

# cProfile здесь даже на 50 000 циклов выдает НУЛИ.


# ИТОГ: Второй вариант оказался существенно более выгодным по асимптотике и скорости работы. При этом оказалось, что
# таймит сам по себе сжирает кучу времени (cProfile прогонял тест на 50 000 циклов в первом варианте решения очень
#  быстро,в то время как таймит долго тупил даже на 5000). Честно говоря, почему первый код так медленно обрабатывается,
#  я так и не понял - но как проводить проверку осознал. Второй вариант решения имеет идеальную скорость работы и его
#  кривая по времени растет линейно и очень медленно.
