class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p

    def addHead(self, item):
        p = Node(item)
        p.next = self.head
        self.head = p

    def search(self, item):
        p = self.head
        while p != None:
            if p.value == item:
                return True
            else:
                p = p.next
        return False

    def index(self, item):
        p = self.head
        count = 0
        while p != None:
            if p.value == item:
                return count
            else:
                p = p.next
                count +=1
        return -1

    def size(self):
        if (self.head == None):
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
            elif pos > self.size()-1:
                return 'Out of Range'
            else:
                for i in range(pos-1):
                    p = p.next
                p.next = p.next.next

            return 'Success'
        else:
            return 'Out of Range'

    def insert(self,pos,item):
        if self.head != None:
            p = self.head
            n = Node(item)
            if pos > self.size():
                for i in range (self.size()):
                    p = p.next
                p.next = n
                return
            elif pos < 0:
                if 0 - pos > self.size() - 1:
                    self.addHead(item)
                    return
                else:
                    pos = self.size() - 1 + pos
            for i in range(pos):
                p = p.next
            q = p.next
            p.next = n
            n.next = q
        else:
            self.head = item


inp = input('Enter Input : ').split(',')
L = LinkedList()
L.append('|')

for i in inp:
    i = i.split(' ')
    if i[0] == 'I':
        L.insert(L.index('|')-1,i[1])
    elif i[0] == 'L':
        pos = L.index('|')
        if pos > 1:
            L.pop(pos)
            L.insert(pos -2,'|')
        elif pos == 1:
            L.pop(pos)
            L.addHead('|')
    elif i[0] == 'R':
        pos = L.index('|')
        if pos + 1 == L.size():
            pass
        else:
            L.pop(pos)
            L.insert(pos,'|')
    elif i[0] == 'B':
        pos = L.index('|')
        if pos == 0:
            pass
        else:
            L.pop(pos-1)
    elif i[0] == 'D':
        pos = L.index('|')
        if pos == L.size()-1:
            pass
        else:
            L.pop(pos+1)
print(L)
