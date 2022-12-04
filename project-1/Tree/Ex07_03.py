class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self,n=0,root=None):
        self.root = root
        self.n = n
        for i in range(n//2):
            self.insert(0)

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
        else:
            q = [self.root]
            while len(q) != 0:
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                else:
                    curr.left = new
                    break
                if curr.right:
                    q.append(curr.right)
                else:
                    curr.right = new
                    break
        return self.root


    def postOrder(self,root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            minValue = 0
            if root.left and root.right:
                minValue = min(root.left.data,root.right.data)
                root.left.data -= minValue
                root.right.data -= minValue
                root.data = minValue
            elif root.left and not root.right:
                minValue = root.left.data
                root.left.data -= minValue
                root.data = minValue
            elif root.right and not root.left:
                minValue = root.right.data
                root.right.data -= minValue
                root.data = minValue

    def preOrder(self, root,arr):
        if root is not None:
            arr.append(root.data)
            self.preOrder(root.left,arr)
            self.preOrder(root.right,arr)
        return arr

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


inp = input('Enter Input : ').split('/')
size = int(inp[0])
data = list(map(int,inp[1].split()))

if len(data) != (size//2) + 1:
    print('Incorrect Input')
else:
    T = Tree(size)
    for i in data:
        T.insert(i)
    T.postOrder(T.root)
    ans = T.preOrder(T.root,[])
    print(sum(ans))