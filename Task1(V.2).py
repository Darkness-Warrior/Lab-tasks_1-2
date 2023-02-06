class Math:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.a and self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not allowed"

    def subtraction(self):
        return self.a - self.b


primer_1 = Math(10, 0)
primer_2 = Math(10, 2)
print(primer_1.addition())
print(primer_1.multiplication())
print(primer_1.division())
print(primer_1.subtraction())
print(primer_2.division())