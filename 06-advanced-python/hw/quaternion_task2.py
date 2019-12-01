from math import sqrt


class Quaternion:
    """Класс Quaternion, позволяющий работать с кватернионами"""

    def __init__(self, a=0, i=0, j=0, k=0):
        self.a = a
        self.i = i
        self.j = j
        self.k = k

    def __repr__(self):
        return '({} + {}i, {}j, {}k)'.format(self.a, self.i, self.j, self.k)

    def __str__(self):
        return '({} + {}i, {}j, {}k)'.format(self.a, self.i, self.j, self.k)

    def __add__(self, other):
        if isinstance(other, Quaternion):
            a = self.a + other.a
            i = self.i + other.i
            j = self.j + other.j
            k = self.k + other.k

            return Quaternion(a, i, j, k)

        elif isinstance(other, (float, int)):
            raise Exception

    def __eq__(self, other):
        return self.a == other.a and self.i == other.i and self.j == other.j and self.k == other.k 

    def __abs__(self):
        square = self.a * self.a + self.i * self.i + self.j * self.j + self.k * self.k
        return sqrt(square)

    def __mul__(self, other):

        if isinstance(other, Quaternion):
            a1, a2 = self.a, other.a
            b1, b2 = self.i, other.i
            c1, c2 = self.j, other.j
            d1, d2 = self.k, other.k

            a = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
            i = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
            j = a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2
            k = a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2

            return Quaternion(a, i, j, k)

        elif isinstance(other, (float, int)):
            return Quaternion(self.a * other, self.i * other, self.j * other, self.k * other)

    def __truediv__(self, other):
        if isinstance(other, Quaternion):
            adjacent = Quaternion(other.a, - other.i, - other.j, - other.k)
            norm_q = abs(other) * abs(other)
            mul = adjacent / norm_q
            return self * mul
        elif isinstance(other, (float, int)):
            if other == 0:
                print("no division by zero")
                return
            return Quaternion(self.a / other, self.i / other, self.j / other, self.k / other)
