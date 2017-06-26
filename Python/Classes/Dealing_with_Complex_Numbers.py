import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, second):
        return Complex(self.real + second.real,
                       self.imaginary + second.imaginary)

    def __sub__(self, second):
        return Complex(self.real - second.real,
                       self.imaginary - second.imaginary)

    def __mul__(self, second):
        return Complex(self.real*second.real - self.imaginary*second.imaginary,
                       self.real * second.imaginary + second.real * self.imaginary)

    def __div__(self, second):
        numerator = Complex(self.real, self.imaginary)*Complex(second.real, -second.imaginary)
        denominator = Complex(second.real, second.imaginary)*Complex(second.real, -second.imaginary)
        return Complex(numerator.real/denominator.real, numerator.imaginary/denominator.real)

    def mod(self):
        return Complex(math.sqrt(pow(self.real, 2) + pow(self.imaginary, 2)), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

