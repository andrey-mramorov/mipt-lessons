class Complex:
    Re = ''
    Im = ''

    def __init__(self, real, imagine):
        self.Re = real
        self.Im = imagine

    def __abs__(self):
        return (self.Re**2 + self.Im**2)**0.5

    def __add__(self, other):
        return Complex(self.Re + other.Re, self.Im + other.Im)

    def __radd__(self, other):
        return Complex(self.Re + other.Re, self.Im + other.Im)

    def __sub__(self, other):
        return Complex(self.Re - other.Re, self.Im - other.Im)

    def __str__(self):
        return '('+str(self.Re)+'+'+str(self.Im)+'j'+')'

    def __repr__(self):
        return 'Complex('+str(self.Re)+', '+str(self.Im)+')'


z = Complex(10, 10)
print(z)
print(z.__repr__())
print(eval(repr(z)))
