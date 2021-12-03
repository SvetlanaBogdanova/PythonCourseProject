class Complex:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __str__(self):
        sign = '+' if self.im >= 0 else '-'
        return f'{self.re} {sign} {abs(self.im)}i'


my_complex_1 = Complex(3, 1)
my_complex_2 = Complex(2, -3)
print(my_complex_1 + my_complex_2)
print(my_complex_1 * my_complex_2)
