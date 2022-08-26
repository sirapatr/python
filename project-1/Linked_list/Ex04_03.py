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
                q = self.head.value
                self.head = p.next
                return q
            elif pos > self.size()-1:
                return 'Out of Range'
            else:
                for i in range(pos-1):
                    p = p.next
                q = p.next.value
                p.next = p.next.next

            return q
        else:
            return 'Out of Range'


v= input('Enter Input (L1,L2) : ')
v = v.split(' ')
l1 = v[0].split('->')
l2 = v[1].split('->')
L1 = LinkedList()
L2 = LinkedList()
for i in l1:
    L1.append(i)
for i in l2:
    L2.append(i)

print('L1    :',L1)
print('L2    :',L2)
while not L2.isEmpty():
    L1.append(L2.pop(L2.size()-1))

print('Merge :',L1)