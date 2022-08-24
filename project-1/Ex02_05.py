class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

print("******** Parking Lot ********")

m, s, o, n = input("Enter max of car,car in soi,operation : ").split()

m, n = int(m), int(n)

S1 = Stack()
S2 = Stack()
L = s.split(',')
a = False

for i in L:
    if i != '0':
        S1.push(int(i))


if o == 'arrive':
    if m > S1.size() :
        for i in range(S1.size()):
            k = S1.pop()
            S2.push(k)
            if k == n:
                print('car',n,'already in soi')
                a = True
                break
        while not S2.isEmpty():
            S1.push(S2.pop())
        if not a:
            S1.push(n)
            print('car',n,'arrive! : Add Car',n)
    else:
        print("car", n, "cannot", o, ": Soi Full")
else:
    if S1.size() >0:
        for i in range(S1.size()):
            k = S1.pop()
            S2.push(k)
            if k == n:
                S2.pop()
                print('car',n,'depart ! : Car',n,'was remove')
                a = True
                break
        while not S2.isEmpty():
            S1.push(S2.pop())
        if not a:
            print('car',n,'cannot depart : Dont Have Car',n)
    else:
        print('car',n,'cannot depart : Soi Empty')


print(S1.items)
    ### Enter Your Code Here ###

