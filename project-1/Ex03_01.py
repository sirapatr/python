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


    def __str__(self):
        print()

v = input('Enter Input : ').split(',')
q = Queue()


for i in v :
    if(i == 'D'):
        if q.isEmpty():
            print('-1')
        else:
            print(q.deQueue(),end=' ')
            print('0')
    else:
        x = i.split(' ')
        q.push(int(x[1]))
        print(q.size())

if q.isEmpty():
    print('Empty')
else:
    while not q.isEmpty():
        print(q.deQueue(),end=' ')

