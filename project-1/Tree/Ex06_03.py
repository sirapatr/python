class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        p = self.root
        while True:
            if data < p.data:
                if p.left is None:
                    p.left = Node(data)
                    return
                p = p.left
            else:
                if p.right is None:
                    p.right = Node(data)
                    return
                p = p.right

    def inOrder(self,root,data):
        if root is not None:
            self.inOrder(root.left,data)
            if root.data > data:
                root.data *= 3
            self.inOrder(root.right,data)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split('/')
inp1 = [int(i) for i in inp[0].split()]
for i in inp1:
    T.insert(i)
T.printTree(T.root)
print('--------------------------------------------------')
T.inOrder(T.root,int(inp[1]))
T.printTree(T.root)