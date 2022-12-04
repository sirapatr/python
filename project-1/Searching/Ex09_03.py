class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,table,size,maxCollission):
        self.size = size
        self.maxCollission = maxCollission
        self.table = table


    def insert (self,data):
        count = 1
        key = self.sumOfASCII(data) % self.size

        if self.isFull():
            print('This table is full !!!!!!')
            return -1

        while self.table[key] is not None:
            print('collision number',count,'at',key)
            if count >= self.maxCollission:
                print('Max of collisionChain')
                break
            key = (self.sumOfASCII(data)+ pow(count,2))%self.size
            count +=1

        if self.table[key] is None and count <= self.maxCollission:
            self.table[key] = data
        self.printTable()



    def sumOfASCII (self,data):
        val = 0
        for i in data.key:
            val += ord(i)
        return val

    def printTable (self):
        for i in range(self.size):
            print('#',i+1,'	',self.table[i],sep='')
        print('---------------------------')



    def isFull (self):
        for i in self.table:
            if i is None:
                return False
        return True


print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
size, col = map(int, inp[0].split())
n = inp[1].split(',')
table = [None] * size
hashTable = hash(table,size, col)

for i in n:
    d = i.split()
    full = hashTable.insert(Data(d[0],d[1]))
    if full == -1:
        break