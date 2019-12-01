'''Написать профилирующий декоратор.

Написать функцию-декоратор, которая подсчитывает суммарное количество вызовов
декорируемой функции и общее время, затраченное на исполнение этой функции по
всем вызовам и сохраняет эти данные в глобальную переменную, имя которой
передаётся декоратору. Проверить при помощи этой функции время исполнения
различных алгоритмов поиска чисел фиббоначи. Найти наиболее оптимальный
метод.'''


from time import perf_counter


def call_counter(name):
    def wrapper(func):
        def helper(x):
            start = perf_counter()
            globals()[name]['count'] += 1
            end = perf_counter()
            globals()[name]['performance'] += end - start
            return func(x)
        return helper
    return wrapper


@call_counter('name_1')
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@call_counter('name_2')
def fib2(n):
    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0+f1
    return f1

name_1 = {'count': 0, 'performance': 0}
name_2 = {'count': 0, 'performance': 0}

print(fibonacci(5), name_1)
print(fib2(5), name_2)

if name_1['performance'] < name_2['performance']:
    print('Наиболее оптимальный:', 'fibonacci')
else:
    print('Наиболее оптимальный:', 'fib2')
