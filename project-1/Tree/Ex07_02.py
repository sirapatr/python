class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class AVL:
    def __init__(self):
        self.root = None

    def insert(self,data,node):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.insert(data,node.left)
        if data >= node.data:
            node.right = self.insert(data,node.right)

        bal = self.hight(node.left)-self.hight(node.right)
        if bal > 1 and data < node.left.data:
            return self.rightRoll(node)
        if bal < -1 and data >= node.right.data:
            return self.leftRoll(node)
        if bal > 1 and data >= node.left.data:
            node.left = self.leftRoll(node.left)
            return self.rightRoll(node)
        if bal < -1 and data < node.right.data:
            node.right = self.rightRoll(node.right)
            return self.leftRoll(node)
        return node



    def hight(self,node):
        if not node:
            return 0
        left = self.hight(node.left)
        right = self.hight(node.right)
        if left > right:
            return left + 1
        else:
            return right + 1

    def leftRoll (self,node):
        roll = node.right
        T = roll.left
        roll.left = node
        node.right = T
        return roll


    def rightRoll(self,node):
        roll = node.left
        T = roll.right
        roll.right = node
        node.left = T
        return roll


    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


tree = AVL()
inp = input('Enter Input : ').split()
for i in inp:
    print('Insert : (',i,')')
    tree.root = tree.insert(int(i),tree.root)
    tree.printTree(tree.root)
    print('--------------------------------------------------')