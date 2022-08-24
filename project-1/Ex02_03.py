class Stack:
    def __init__(self):
        self.items = []
        self.count = 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def top(self):
        return self.items[-1]

    def suTop(self,value):
        if self.items[-1] == self.items[-2] and self.items[-1] == value:
            self.pop()
            self.pop()
            self.count += 1
        else:
            self.push(value)

    def size(self):
        return len(self.items)

    def __str__(self):
        return ''.join(self.items)


inp = input('Enter Input : ').split()
S = Stack()
for i in inp:
    if S.size() < 2:
        S.push(i)
    else:
        S.suTop(i)

k = S.size()
print(k)

for i in range(k):
    print(S.pop(),end='')
    if i == k-1:
        print()

if k == 0:
    print("Empty")
if S.count > 1 :
    print("Combo :",S.count,"! ! !")

### Enter Your Code Here ###