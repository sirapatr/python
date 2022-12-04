class hash:
    def __init__(self,table,size,maxCollission,Threshold):
        self.size = size
        self.maxCollission = maxCollission
        self.table = table
        self.Treshold = Threshold




    def insert(self,data):
        for i in range(len(data)):
            print('Add :',data[i])
            dataSize = (self.size * self.Treshold) // 100
            if self.itemCount() < dataSize:
                check = self._insert(data[i])
            else:
                print('****** Data over threshold - Rehash !!! ******')
                check = False

            if not check:
                self.size = nextPrime(self.size*2)
                self.table = [None]*self.size
                for j in range(i+1):
                    self._insert(data[j])
                self.printTable()
            else:
                self.printTable()




    def _insert (self,data):
        count = 1
        key = data % self.size

        while self.table[key] is not None:
            print('collision number',count,'at',key)
            if count >= self.maxCollission:
                print('****** Max collision - Rehash !!! ******')
                return False
            key = (data+ pow(count,2))%self.size
            count +=1

        if self.table[key] is None and count <= self.maxCollission:
            self.table[key] = data
        return True


    def printTable (self):
        for i in range(self.size):
            print('#',i+1,'	',self.table[i],sep='')
        print('----------------------------------------')


    def itemCount (self):
        count = 0
        for i in self.table:
            if i is not None:
                count += 1
        return count

def isPrime (n):
    for i in range(2,int(n**0.5) +1):
        if n % i == 0:
            return False
    return True

def nextPrime (n):
    if n < 1 :
        return 2
    prime = n
    found = False
    while not found:
        prime += 1
        if isPrime(prime):
            found = True
    return prime

print(' ***** Rehashing *****')
inp = input('Enter Input : ').split('/')
print('Initial Table :')
size, col, Thres = map(int, inp[0].split())
n = list(map(int , inp[1].split()))
table = [None] * size
hashTable = hash(table,size, col,Thres)
hashTable.printTable()
hashTable.insert(n)