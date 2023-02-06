class A:
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2

    def method_1(self):
        print("Method 1 of class A")

    def method_2(self):
        print("Method 2 of class A")

    def method_3(self):
        print("Method 3 of class A")


class B(A):
    def __init__(self, prop1, prop2, prop3):
        super().__init__(prop1, prop2)
        self.prop3 = prop3

    def method_3(self):
        print("Method 3 of class B")


class C(A):
    def __init__(self, prop1="default_prop1", prop2="default_prop2"):
        super().__init__(prop1, prop2)

    def method_4(self):
        print("Method 4 of class C")

    def method_5(self):
        print("Method 5 of class C")


a = A("prop1_value", "prop2_value")
b = B("prop1_value", "prop2_value", "prop3_value")
c = C()

a.method_1()
a.method_2()
a.method_3()

b.method_1()
b.method_2()
b.method_3()

c.method_1()
c.method_2()
c.method_3()
c.method_4()
c.method_5()