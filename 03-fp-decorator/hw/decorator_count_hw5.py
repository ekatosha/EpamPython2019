'''Написать профилирующий декоратор.

Написать функцию-декоратор, которая подсчитывает суммарное количество вызовов
декорируемой функции и общее время, затраченное на исполнение этой функции по
всем вызовам и сохраняет эти данные в глобальную переменную, имя которой
передаётся декоратору. Проверить при помощи этой функции время исполнения
различных алгоритмов поиска чисел фиббоначи. Найти наиболее оптимальный
метод.'''


from time import perf_counter
import numpy as np


def call_counter(name):
    def wrapper(func):
        def helper(x):
            start = perf_counter()
            globals()[name]['count'] += 1
            end = perf_counter()
            globals()[name]['performance'] += end - start
            return func(x)
        helper.__name__ = func.__name__
        return helper
    return wrapper


@call_counter('fib_recursive')
def fib_rec(num):
    if num < 2:
        return num
    return fib_rec(num - 1) + fib_rec(num - 2)


@call_counter('fib_dynamic')
def fib_d(n):
    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0+f1
    return f1


@call_counter('fib_matrix')
def fib_m(n):
    matrix = np.mat ([[1, 1], [1, 0]])
    w, v = np.linalg.eig (matrix)
    d = np.diag(w**n)
    v_inv = np.linalg.inv(v)
    result = v @ d @ v_inv
    return int(result[0, 1])



fib_recursive = {'count': 0, 'performance': 0}
fib_dynamic = {'count': 0, 'performance': 0}
fib_matrix = {'count': 0, 'performance': 0}

print(fib_rec(10), fib_rec.__name__, fib_recursive)
print(fib_d(10),  fib_d.__name__, fib_dynamic)
print(fib_m(10), fib_m.__name__, fib_matrix)

min_performance = min(fib_recursive['performance'], fib_dynamic['performance'], fib_matrix['performance'])
if min_performance in fib_recursive:
    print('Самая быстрая функция:', fib_rec.__name__, fib_recursive['performance'])
elif min_performance in fib_dynamic:
    print('Самая быстрая функция:', fib_d.__name__, fib_dynamic['performance'])
else:
    print('Самая быстрая функция:', fib_m.__name__, fib_matrix['performance'])
