class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, ele):
        self.items.append(ele)

    def insertQueue(self, ele, lo):
        self.items.insert(lo, ele)

    def deQueue(self):
        x = ''
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

    def peek(self,val):
        return self.items[val]

    def searchQueue(self, platform):
        for i in range(self.size()):
            if self.items[i] == platform:
                return i
        return False

    def __str__(self):
        return self.items


stork, command = input('Enter Input : ').split('/')
q = Queue()
id = Queue()

stork = stork.split(',')
command = command.split(',')

for k in command:
    i = k.split(' ')
    if i[0] == 'D':
        if not q.isEmpty():
            print(q.deQueue())
            id.deQueue()
        else:
            print('Empty')
    elif i[0] == 'E': # i = [E , 101]
        for j in stork:
            j = j.split(' ')    # j = [1 , 101]
            if i[1] == j[1]:
                if q.isEmpty():
                    q.enQueue(i[1])
                    id.enQueue(j[0])
                else:
                    lo = id.searchQueue(j[0])
                    for a in range(id.size()-1,-1,-1):
                            if a <= lo:
                                q.enQueue(i[1])
                                id.enQueue(j[0])
                                break
                            elif j[0] == id.items[a-1]:
                                q.insertQueue(i[1],a)
                                id.insertQueue(j[0],a)
                                break




