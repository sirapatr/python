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

    def insert(self,data,node = None):
        if self.root is None:
            self.root = Node(data)
            return

        if node is not None:
            cur = node
        else:
            cur = self.root
        re = [0,0]
        if cur.data > data:
            if cur.left is None:
                cur.left = Node(data)
                re[0] +=1
                return re
            else:
                re = self.insert(data,cur.left)
                if cur.right is None:
                    re[0] += 1
        else:
            if cur.right is None:
                cur.right = Node(data)
                re[0] -= 1
                return re
            else:
                re = self.insert(data,cur.right)
                if cur.left is None:
                    re[0] -= 1
        print(re,cur.data)
        print()
        self.printTree(self.root)
        print()

        if re[1] == 1:
            if re[0] > 1:
                node = cur.left.left
                self.rollLeft(cur.left)
                cur.left = node
                re[0] -= 1
                re[1] = 0
            elif re[0] == 1 and node is None:
                self.rollLeft(cur)
            elif re[0] == -1 and node is None:
                self.rollRight(cur)
            elif re[0] < -1:
                node = cur.right.right
                self.rollRight(cur.right)
                cur.right = node
                re[0] += 1
                re[1] = 0
        elif node is None:
            if re[0] > 1:
                self.rollLeft(cur)
                re[0] -= 1
            elif re[0] < -1:
                self.rollRight(cur)
                re[0] += 2

        else:
            re[1] = 1
            return re
        return re



        # re = 0
        # if node.data <= data:
        #     if node.right is None:
        #         node.right = Node(data)
        #         return -1
        #     else:
        #         re = self.insert(node.right,data)
        #         if node.left is None:
        #             re -=1
        #         else:
        #             re +=1
        # else:
        #     if node.left is None:
        #         node.left = Node(data)
        #         return 1
        #     else:
        #         re = self.insert(node.left,data)
        #         if node.right is None:
        #             re += 1
        #         else:
        #             re -=1
        # print('re',re)
        # return re



    def rollLeft (self,node):
        cur = node
        roll = cur.left
        cur.left = roll.right
        roll.right = cur
        if cur == self.root:
            self.root = roll

    def rollRight(self,node):
        cur = node
        roll = cur.right
        cur.right = roll.left
        roll.left = cur
        if cur == self.root:
            self.root = roll

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


tree = AVL()
inp = input('Enter Input : ').split()
for i in inp:
    print('Insert : (',i,')')
    tree.insert(int(i))
    tree.printTree(tree.root)
    print('--------------------------------------------------')