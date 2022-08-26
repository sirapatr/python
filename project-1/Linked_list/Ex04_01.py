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

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        if L.search(i[3:]):
            print("Found {0} in {1}".format(i[3:],L))
        else:
            print("Not Found {0} in {1}".format(i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)