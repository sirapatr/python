class Node:
    def __init__(self, key,value = 0, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return f"N({self.key},{self.value})"

def getKey(x):
    if x.key == '*':
        return 0
    else:
        return ord(x.key)

def printHuffman(node,s = ''):
    m = ''
    if node.right is not None:
        m +=printHuffman(node.right,s+'1') + '*'
    if node.left is not None:
        m += printHuffman(node.left,s+'0')+'*'
    if node.key != '*':
        last = list(s)
        isLast = True
        for i in s:
            if i == '1':
                isLast = False
        if isLast:
            print('\'', node.key, '\': \'', s, '\'', sep='', end='')
            m += node.key + ',' + s
            return m
        else:
            print('\'',node.key,'\': \'',s,'\',',sep='',end=' ')
            m += node.key + ',' + s
            return m
    return m

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)



inp = list(input('Enter Input : '))
data = list(inp)
data.sort()
s = []
for i in data:
    if s:
        if s[-1].key == i:
            s[-1].value += 1
        else:
            s.append(Node(i,1))
    else:
        s.append(Node(i,1))

while len(s)>1:
    s.sort(key=getKey)
    s.sort(key=lambda a: a.value)
    x = s.pop(0)
    y = s.pop(0)
    val = x.value + y.value
    cur = Node('*',val,x,y)
    s.append(cur)


Tree = s.pop()
print('{',end='')
m = printHuffman(Tree).split('*')
print('}')
printTree90(Tree)
print('Encoded! : ',end='')
for i in inp:
    for k in m:
        if i == k[:1]:
            print(k[2:],end='')