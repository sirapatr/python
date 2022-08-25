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
    elif i[0] == 'E':
        for j in stork:
            check = j.split(' ')
            if i[1] == check[1]:
                if q.isEmpty():
                    q.enQueue(i[1])
                    id.enQueue(check[0])
                else:
                    cut = False
                    for l in range(id.size()):
                        if cut:
                            q.insertQueue(i[1], l)
                            id.insertQueue(check[0], l)
                        else:
                            if id.items[l] == check[0]:
                                if id.items[l+1] != check[0]:
                                    cut = True
                            else:
                                q.enQueue(i[1])
                                id.enQueue(check[0])

