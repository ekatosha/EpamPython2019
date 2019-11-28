'''Гипотеза Коллатца
Гипотеза может быть кратко выражена следующим образом:

берём любое натуральное число n, если оно чётное, то делим его на 2
если нечётное, то умножаем на 3 и прибавляем 1 (получаем 3n + 1)
над полученным числом выполняем те же самые действия, и так далее
Гипотеза Коллатца заключается в том, что какое бы начальное число n мы ни взяли, рано или поздно мы получим единицу.

Пример
Для числа 12:

12 6 3 10 5 16 8 4 2 1

Всего получаем 9 шагов.

Задача
Вычислить число шагов для числа n, согласно гипотезе Коллатца необходимых для достижения этим числом единицы, используя функциональный стиль. По возможности не забыть проверить пограничные условия и входные данные.

def collatz_steps(n):
 ...

 assert collatz_steps(16) == 4
 assert collatz_steps(12) == 9
 assert collatz_steps(1000000) == 152 '''


def even_odd(num_d):
    if num_d['number']%2 == 0:
        return {'number': num_d['number']//2,
            'count': num_d['count'] + 1}
    return {'number': num_d['number']*3+1,
            'count': num_d['count'] + 1}

def make_d(num):
    return {'number': num, 'count': 0}

def step(state):
    if state['number'] == 1:
        return state['count']
    return step(even_odd(state))

def collatz_steps(n):
    if not isinstance(n, int):
        raise TypeError('an integer is required')
    if n <= 0:
        raise ValueError('n > 0 is required')
    return step(make_d(n))


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152
