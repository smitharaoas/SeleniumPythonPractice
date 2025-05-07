class Calculator:
    num = 50

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Called by default")

    def getData(self):
        print("Method in class")

    def summation(self):
        return self.a + self.b


obj = Calculator(2, 3)
obj.getData()
print("Class variable is")
print(obj.num)
print(obj.summation())

obj1 = Calculator(4, 5)
print(obj1.summation())
