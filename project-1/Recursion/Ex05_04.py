def printHanoi(nmax, a=['A'], b=['B'], c=['C']):
    fir = check('A', a, b, c)
    sec = check('B', a, b, c)
    thr = check('C', a, b, c)
    try:
        print(fir[nmax], end=' ')
    except:
        print('| ', end='')
    try:
        print(sec[nmax], end=' ')
    except:
        print('| ', end='')
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


def move(n, s_pole, d_pole, i_pole, nmax):
    if n == 1:
        print("Move 1 from", s_pole[0], "to", d_pole[0])
        d_pole.append(s_pole.pop())
        printHanoi(nmax,s_pole,d_pole,i_pole)
        return
    move(n - 1, s_pole, i_pole, d_pole, nmax)
    print("Move", n, "from", s_pole[0], "to", d_pole[0])
    d_pole.append(s_pole.pop())
    printHanoi(nmax, s_pole, d_pole, i_pole)
    move(n - 1, i_pole, d_pole, s_pole, nmax)


n = int(input("Enter Input : "))
a = genaratetower(n)
printHanoi(n + 1, a)
move(n, a, ['C'], ['B'], n + 1)
