class Stack:
    def __init__(self):
        self.items = []

    def push(self, ele):
        self.items.append(ele)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def __str__(self):
        print()

class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        operand = ['+','-','*','/']
        s = Stack()
        for c in data:
            if c in operand:
                x = s.pop()
                y = s.pop()
                node = Node(c,y,x)
                s.push(node)
                self.root = node
            else:
                s.push(Node(c))

    def inOrder(self,root):
        if root is not None:
            operand = ['+', '-', '*', '/']
            if root.data in operand:
                print('(',end='')
            self.inOrder(root.left)
            print(root.data,end='')
            self.inOrder(root.right)
            if root.data in operand:
                print(')',end='')

    def preOrder(self,root):
        if root is not None:
            print(root.data,end='')
            self.preOrder(root.left)
            self.preOrder(root.right)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = input('Enter Postfix : ')
T.insert(list(inp))
print('Tree :')
T.printTree(T.root)
print('--------------------------------------------------')
print('Infix : ',end='')
T.inOrder(T.root)
print()
print('Prefix : ',end='')
T.preOrder(T.root)