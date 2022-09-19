def printHanoi(nmax, a=['A'], b=['B'], c=['C']):
    fir = check('A', a, b, c)
    sec = check('B', a, b, c)
    thr = check('C', a, b, c)
    try:
        print(fir[nmax], end='  ')
    except:
        print('| ', end=' ')
    try:
        print(sec[nmax], end='  ')
    except:
        print('| ', end=' ')
    try:
        print(thr[nmax])
    except:
        print('|')
    if nmax > 1:
        printHanoi(nmax - 1, a, b, c)

    # code here
    pass


def check(val, a=[], b=[], c=[]):
    if val == a[0]:
        return a
    elif val == b[0]:
        return b
    else:
        return c


def genaratetower(n, a=['A']):
    a.append(n)
    if n > 1:
        genaratetower(n - 1, a)
    return a


def move(n, A, B, C, nmax):
    if n == 1:
        print("move 1 from ", A[0], "to", B[0])
        B.append(A.pop())
        printHanoi(nmax, A, B, C)
        return
    move(n - 1, A, C, B, nmax)
    print("move", n, "from ", A[0], "to", B[0])
    B.append(A.pop())
    printHanoi(nmax, A, B, C)
    move(n - 1, C, B, A, nmax)


n = int(input("Enter Input : "))
a = genaratetower(n)
printHanoi(n + 1, a)
move(n, a, ['C'], ['B'], n + 1)
