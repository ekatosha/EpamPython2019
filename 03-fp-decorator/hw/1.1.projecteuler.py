import math
from functools import reduce

'''3.1. Special Pythagorean triplet. Problem 9
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

result = [a*b*math.sqrt(a**2+b**2) for a in range(1000) for b in range(1000) if a+b+math.sqrt(a**2+b**2) == 1000 and a*b*math.sqrt(a**2+b**2) !=0]
print(result[0])

'''3.1.Sum square difference. Problem 6
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

# Var 1
result_2 = sum([x for x in range(101)])**2 - sum([x**2 for x in range(101)])
print(result_2)

# Var 2
result_2_1 = (reduce((lambda x, y: x + y), range(101)))**2 - reduce((lambda x, y: x + y), [i**2 for i in range(101)])
print(result_2_1)

# Var 3
n = 100
print((n**2 * (n+1)**2 * 1/4) - (n * (n+1)*(2*n+1) * 1/6))

'''3.1.Self powers. Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.'''

result_3 = str(sum([i**i for i in range(1, 1001)]))[-10:]
print(result_3)

'''3.1.Champernowne's constant. Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000'''

# одна строчка
result_4_1 = reduce((lambda x, y: x * y), [int(''.join([str(i) for i in range(1,10000001)])[10**j-1]) for j in range(7)])
print(result_4_1)

# читабельно
my_list = ''.join([str(i) for i in range(1, 10000001)])
result_4_2 = reduce((lambda x, y: x * y), [int(my_list[10**j-1]) for j in range(7)])
print(result_4_2)
