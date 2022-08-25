class funString():

    def __init__(self, aString):
        self.aString = aString
        self.aList = list(aString)

    def __str__(self):
        print('hi')

    def size(self) :
        return len(self.aString)

    def changeSize(self):
        return self.aString.swapcase()

    def reverse(self):
        l = self.aList[::-1]
        return ''.join(l)

    def deleteSame(self):
        l = list(dict.fromkeys(self.aList))
        return ''.join(l)



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())