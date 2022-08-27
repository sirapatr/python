class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, str(self.head.value) + " "
        while cur.next is not None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head is None

    def append(self, item):
        p = Node(item)
        if self.head is None:
            self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p

    def addHead(self, item):
        p = Node(item)
        p.next = self.head
        self.head = p

    def popHead(self):
        p = self.head
        q = p.value
        self.head = p.next
        return q

    def search(self, item):
        p = self.head
        while p is not None:
            if p.value == item:
                return True
            else:
                p = p.next
        return False

    def index(self, item):
        p = self.head
        count = 0
        while p is not None:
            if p.value == item:
                return count
            else:
                p = p.next
                count += 1
        return -1

    def size(self):
        if self.head == None:
            return 0
        else:
            count = 0
            p = self.head
            while (p != None):
                p = p.next
                count += 1
            return count

    def pop(self, pos):
        if self.head != None:
            p = self.head
            if pos == 0:
                self.head = p.next
            elif pos > self.size() - 1:
                return 'Out of Range'
            else:
                for i in range(pos - 1):
                    p = p.next
                p.next = p.next.next

            return 'Success'
        else:
            return 'Out of Range'

    def insert(self, pos, item):
        if self.head != None:
            p = self.head
            n = Node(item)
            if pos > self.size():
                for i in range(self.size()):
                    p = p.next
                p.next = n
                return
            elif pos < 0:
                if 0 - pos > self.size() - 1:
                    self.addHead(item)
                    return
                else:
                    pos = self.size() - 1 + pos
            elif pos == 0:
                self.addHead(item)
                return
            for i in range(pos - 1):
                p = p.next
            q = p.next
            p.next = n
            n.next = q
        else:
            self.head = item

    def __getitem__(self, index):
        if self.isEmpty():
            return None
        p = self.head
        for _ in range(index):
            p = p.next
        return p.value


def isOver(Linked, num):
    for i in range(Linked.size()):
        if Linked[i] > num:
            Linked.insert(i, num)
            return
    Linked.append(num)


def sort(num, Ro):
    num1 = abs(num)
    for _ in range(Ro):
        num1 //= 10
    val = num1 % 10
    isOver(Radix[val], num)


def printSort(Ro):
    print('------------------------------------------------------------')
    print('Round :', Ro + 1)
    for i in range(10):
        print(i, ':', Radix[i])


def collectSort():
    for i in range(10):
        while not Radix[i].isEmpty():
            L.append(Radix[i].popHead())


Radix = LinkedList()
for _ in range(10):
    Radix.append(LinkedList())

L = LinkedList()
inp = input('Enter Input : ').split()
maxRound = 0
Round = 0

for i in inp:
    if maxRound < len(i):
        maxRound = len(i)
    L.append(int(i))

Lsize = L.size()
while Round <= maxRound:
    while not L.isEmpty():
        sort(L.popHead(), Round)
    printSort(Round)
    if Radix[0].size() == Lsize:
        collectSort()
        break
    collectSort()
    Round += 1

print('------------------------------------------------------------')
print(Round, 'Time(s)')
print('Before Radix Sort : ', end='')
for i in range(len(inp)):
    if i == len(inp) - 1:
        print(inp[i])
    else:
        print(inp[i], end=' -> ')
print('After  Radix Sort : ', end='')

for i in range(Lsize):
    if i >= Lsize - 1:
        print(L.popHead())
    else:
        print(L.popHead(), end=' -> ')
