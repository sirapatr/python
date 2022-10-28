class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
        self.rank = 0

    def insert (self, data):
        if self.root is None:
            self.root = Node(data)
            self.rank += 1
            return

        h = height(self.root)
        maxNode = pow(2,h+1) -1
        cur = self.root

        if self.rank +1 > maxNode:
            while cur.left is not None:
                cur = cur.left
            cur.left = Node(data)
            self.rank +=1

        elif self.rank +1 == maxNode:
            while cur.right is not None:
                cur = cur.right
            cur.right = Node(data)
            self.rank += 1

        else:
            if self.rank +1 <= maxNode - ((maxNode - (pow(2, h) - 1)) / 2):
                self.subInsert(data,cur.left,self.rank - round(pow(2, h) / 2))
            else:
                self.subInsert(data,cur.right,self.rank - pow(2,h))
            self.rank += 1

    def subInsert(self,data,node,rank):
        if node != None:
            h = height(node)
            maxNode = pow(2,h+1)-1
            cur = node

            if node == None:
                return
            if rank +1 > maxNode:
                while cur.left is not None:
                    cur = cur.left
                cur.left = Node(data)
                return
            elif rank +1 == maxNode:
                while cur.right is not None:
                    cur = cur.right
                cur.right = Node(data)
                return
            if rank + 1 <= maxNode - ((maxNode - (pow(2, h) - 1)) / 2):
                self.subInsert(data, cur.left, rank - round(pow(2, h) / 2))
            else:
                self.subInsert(data, cur.right, rank - pow(2, h))

        else:
            return

    def sumPower (self, node):
        power = node.data
        if node.left is not None:
            power += self.sumPower(node.left)
        if node.right is not None:
            power += self.sumPower(node.right)
        return power

def move(lo,root):
    cur = root
    s = []
    while lo > 0:
        if lo % 2 == 0:
            lo -= 2
            s.append(1)
        else:
            lo -= 1
            s.append(0)
        lo /= 2
    while len(s) >0:
        if s.pop() == 0:
            cur = cur.left
        else:
            cur = cur.right
    return cur

def height (root):
    if root is None:

        return -1

    else:

        left = height(root.left)

        right = height(root.right)

        if left > right:

            return left + 1

        else:

            return right + 1

tree = Tree()
inp = input('Enter Input : ').split('/')
for i in inp[0].split():
    tree.insert(int(i))
print(tree.sumPower(tree.root))
for i in inp[1].split(','):
    j = i.split()
    x = tree.sumPower(move(int(j[0]),tree.root))
    y = tree.sumPower(move(int(j[1]),tree.root))
    if x > y:
        print(j[0],'>',j[1],sep='')
    elif x < y:
        print(j[0],'<',j[1],sep='')
    else:
        print(j[0],'=',j[1],sep='')
