"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
"""


class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'{self.real}{"+" if self.imag >= 0 else ""}{self.imag}j'

    def __add__(self, other):
        """
        (a + bj) + (c + dj) = (a + c) + (b + d)j
        """
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        """
        (a + bj) * (c + dj) = (ac − bd) + (bc + ad)j
        """
        real = self.real * other.real - (self.imag * other.imag)
        imag = self.imag * other.real + self.real * other.imag
        return ComplexNumber(real, imag)


cn1 = ComplexNumber(12, -2)
cn2 = ComplexNumber(-4, 4)
print(cn1)
print(cn1 + cn2)
print(cn1 * cn2)
