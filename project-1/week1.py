


class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQuene(self, i):
        self.items.append(i)

    def deQuene(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    nBomb, mBomb = input('Enter Input (Normal, Mirror) : ').split(' ')

    nBomb = list(nBomb)
    mBomb = list(mBomb)

    nItem = Queue()
    mItem = Queue()

    sizeN, sizeM = len(nBomb), len(mBomb)

    nflag = True
    mflag = True
    fflag = True
    nCount = 0
    mCount = 0
    fCount = 0

    while sizeM > 2 and mflag is True:
        for i in range(sizeM - 1, -1, -1):
            if mBomb[i] == mBomb[i - 1] == mBomb[i - 2]:
                mItem.enQuene(mBomb[i])
                mBomb.pop(i - 2)
                mBomb.pop(i - 2)
                mBomb.pop(i - 2)
                sizeM -= 3
                mCount += 1
                break
            if i == 0:
                mflag = False

    while sizeN > 2 and nflag is True:
        for i in range(sizeN - 2):
            if nBomb[i] == nBomb[i + 1] == nBomb[i + 2]:
                if mItem.size() > 0:
                    nBomb.insert(i + 2, mItem.deQuene())
                    sizeN += 1
                    fflag = False
                if nBomb[i] == nBomb[i + 1] == nBomb[i + 2]:
                    nBomb.pop(i)
                    nBomb.pop(i)
                    nBomb.pop(i)
                    sizeN -= 3
                    if fflag is True:
                        nCount += 1
                    else:
                        fCount += 1
                fflag = True
                break

            if i == sizeN - 3:
                nflag = False

    while mItem.size() > 0:
        mItem.deQuene()
    if sizeN > 0:
        for i in nBomb:
            nItem.enQuene(i)
    if sizeM > 0:
        for i in mBomb:
            mItem.enQuene(i)

    print('NORMAL :')
    print(sizeN)
    # ''.join(nItem.items)
    n = ''.join(nItem.items)
    print(n[::-1] if sizeN > 0 else 'Empty')
    print(nCount, 'Explosive(s) ! ! ! (NORMAL)')
    if fCount > 0:
        print('Failed Interrupted', fCount, 'Bomb(s)')
    print('------------MIRROR------------')
    print(': RORRIM')
    print(sizeM)
    m = ''.join(mItem.items)
    print(m if sizeM > 0 else 'ytpmE')
    print('(RORRIM) ! ! ! (s)evisolpxE', mCount)