class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head != None:
            p = self.head
            for i in range(self.size()-1):
                p = p.next
            n = Node(item)
            p.next = n
            n.previous = p
            self.tail = n
        else:
            self.head = self.tail = Node(item)


    def addHead(self, item):
        if self.head != None:
            p = self.head
            n = Node(item)
            p.previous = n
            n.next = p
            self.head = n
        else:
            self.head = self.tail =  Node(item)

    def insert(self, pos, item):
        if self.head != None:
            p = self.head
            if pos > self.size():
                p = self.tail
                n = Node(item)
                p.next = n
                n.previous = p
                self.tail = n
                return
            elif pos < 0:
                if 0 - pos > self.size()-1:
                    self.addHead(item)
                    return
                else:
                    pos = self.size()- 1 + pos
            for i in range(pos):
                p = p.next
            q = p.next
            n = Node(item)
            q.previous = p.next = n
            n.next = q
            n.previous = p
            if pos == self.size():
                self.tail = n

        else:
            self.head = self.tail = Node(item)

    def search(self, item):
        p = self.head
        while p != None:
            if p.value == item:
                return 'Found'
            else:
                p = p.next
        return "Not Found"

    def index(self, item):
        p = self.head
        count = 0
        while p != None:
            if p.value == item:
                return count
            else:
                p = p.next
                count += 1
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
            elif pos > self.size() - 1:
                return 'Out of Range'
            else:
                for i in range(pos - 1):
                    p = p.next
                p.next = p.next.next
                p = p.next
                p.previous = p.previous.previous

            return 'Success'
        else:
            return 'Out of Range'

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())