from OopsDemo import Calculator


class Child1(Calculator):

    num2 = 100

    def __init__(self):
        Calculator.__init__(self,10,20)

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()


obj = Child1()

print (obj.getcompletedata())
