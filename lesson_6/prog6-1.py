import math
"""Class has methods that override __add__, __sub__, __mul__ and __abs__"""

class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        _new_real = self.real * other.real - self.imag * other.imag
        _new_imag = self.imag * other.real + self.real * other.imag
        return Complex(_new_real, _new_imag)
    
    def __abs__(self):
        return math.sqrt(self.real*self.real + self.imag * self.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

first = Complex(1, 1)
second = Complex(1, -1)
third = first * second
print(abs(first))