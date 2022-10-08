class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        p = self.root
        while True:
            if val < p.data:
                if p.left is None:
                    p.left = Node(val)
                    return
                p = p.left
            else:
                if p.right is None:
                    p.right = Node(val)
                    return
                p = p.right

    def delete(self, r, data):
        if self.root.data == data:
            p = self.root
            if p.left is None and p.right is None:
                self.root = None
                return
            elif p.right is None:
                self.root = p.left
                return
        if r is None:
            return r

        if data < r.data:
            r.left = self.delete(r.left,data)
        elif data > r.data:
            r.right = self.delete(r.right,data)
        else:
            if r.left is None:
                p = r.right
                r = None
                return p
            elif r.right is None:
                p = r.left
                r = None
                return p
            p = self.findMin(r.right)
            r.data = p.data
            r.right = self.delete(r.right,p.data)
        return r

    def findMin(self,node):
        p = node
        while p.left is not None:
            p = p.left
        return p

    def Search(self,val):
        if self.root is None:
            return False
        p = self.root
        while True:
            if p.data > val:
                if p.left is None:
                    return False
                p = p.left
            elif p.data < val:
                if p.right is None:
                    return False
                p = p.right
            else:
                return True


def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    if i[:1] == 'i':
        print('insert',i[2:])
        tree.insert(int(i[2:]))
        printTree90(tree.root)
    else:
        print('delete',i[2:])
        if tree.Search(int(i[2:])):
            tree.delete(tree.root,int(i[2:]))
        else:
            print('Error! Not Found DATA')
        printTree90(tree.root)
