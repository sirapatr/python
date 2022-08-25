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
        return self.items

v = input('Enter code,hint : ').split(',')
q = Queue()
fir =  list(v[0])
x = ord(v[1]) - ord(fir[0])
for i in fir :
    y = chr(ord(i)+x)
    q.push(y)
    print(q.items)