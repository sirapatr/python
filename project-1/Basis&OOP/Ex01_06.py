class Calculator :

    def __init__(self, num):
        self.num = num
    ### Enter Your Code Here ###

    def __add__(self, other):
        return self.num + other.num
        ###Enter Your Code For Add Number###

    def __sub__(self, other):
        return self.num - other.num
        ###Enter Your Code For Sub Number###

    def __mul__(self, other):
        return self.num * other.num
        ###Enter Your Code For Mul Number###

    def __truediv__(self, other):
        return self.num / other.num
        ###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")