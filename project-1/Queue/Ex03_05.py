class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, ele):
        if ele != '':
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
        return ''.join(self.items)

class Stack:
    def __init__(self):
        self.items = []
        self.count = 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        x = self.items[-1]
        del self.items[-1]
        return x

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def top(self):
        return self.items[-1]

    def suTop(self,value,mir):
        if self.items[-1] == self.items[-2] and self.items[-1] == value:
            if mir != '0':
                self.push(mir)
                self.push(value)
            else:
                self.pop()
                self.count += 1
                return self.pop()
        else:
            self.push(value)
            return ''

    def size(self):
        return len(self.items)

    def __str__(self):
        return ''.join(self.items)

inp = input('Enter Input (Normal, Mirror) : ').split(' ')
nor = list(inp[0])
mir = list(inp[1])
Smir = Stack()
Snor = Stack()
Snor2 = Stack()
Snor3 = Stack()
qMir = Queue()
mir = mir[::-1]
case = False

for i in mir:
    if Smir.size() < 2:
        Smir.push(i)
    else:
        qMir.enQueue(Smir.suTop(i, '0'))

y = qMir.size()

for j in nor:
    if Snor.size() < 2:
        Snor.push(j)
    else:
        if not qMir.isEmpty():
            if Snor.suTop(j,qMir.peek()) != '':
                qMir.deQueue()
        else:
            Snor.suTop(j,'0')

for j in nor:
    if Snor3.size() < 2:
        Snor3.push(j)
    else:
        Snor3.suTop(j,'0')

for i in Snor.items:
    if Snor2.size() < 2:
        Snor2.push(i)
    else:
        Snor2.suTop(i, '0')

print('NORMAL :')
print(Snor2.size())
if not Snor2.isEmpty():
    for i in range(Snor2.size()):
        print(Snor2.pop(),end='')
    print()
else:
    print('Empty')
    if Snor2.count != y:
        case = True


if not case:
    print(Snor.count,'Explosive(s) ! ! ! (NORMAL)')
    if Snor2.count != 0:
        print('Failed Interrupted',Snor2.count,'Bomb(s)')
else:
    print(Snor.count-y, 'Explosive(s) ! ! ! (NORMAL)')
    if Snor2.count == 0:
        print('Failed Interrupted', y, 'Bomb(s)')


print('------------MIRROR------------')
print(': RORRIM')
print(Smir.size())
if not Smir.isEmpty():
    for i in range(Smir.size()):
        print(Smir.pop(),end='')
    print()
else:
    print('ytpmE')
print('(RORRIM) ! ! ! (s)evisolpxE',Smir.count)


