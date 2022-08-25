class Queue:
    def __init__(self):
        self.items = []

    def push(self, ele):
        self.items.append(ele)

    def deQueue(self):
        x = self.items[0]
        del self.items[0]
        return x

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        print()

v = input('Enter Input : ').split(',')
qEn = Queue()
qEs = Queue()

for i in v :
    if i == 'D':
        if not qEs.isEmpty():
            print(qEs.deQueue())
        elif not qEn.isEmpty():
            print(qEn.deQueue())
        else:
            print('Empty')

    else:
        x = i.split(' ')
        if x[0] == 'EN':
            qEn.push(x[1])
        elif x[0] == 'ES':
            qEs.push(x[1])
        else :
            pass