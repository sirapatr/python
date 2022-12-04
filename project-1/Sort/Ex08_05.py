def selection(l):
    for last in range(len(l)-1,0,-1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1,last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last],l[biggest_i] = l[biggest_i],l[last]

def powerSet(s,a):
    set = []
    x = len(s)
    for i in range(1,1 << x):
        set.append([s[j] for j in range(x) if (i & (1 << j))])
    return sortSet(sort(set,a))

def sortSet (l):

    for last in range(len(l) - 1, 0, -1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1, last + 1):
            if len(l[i]) > len(biggest):
                biggest = l[i]
                biggest_i = i
            elif len(l[i]) == len(biggest):
                for j in range (len(biggest)):
                    if l[i][j] < biggest[j]:
                        break
                    elif l[i][j] > biggest[j]:
                        biggest = l[i]
                        biggest_i = i
                        break
        l[last], l[biggest_i] = l[biggest_i], l[last]
    return l


def sort(l,val):
    data = []
    for i in l:
        ans = 0
        for j in i:
            ans += j
        if ans == val:
           data.append(i)
    return data


inp = input('Enter Input : ').split('/')
set = list(map(int,inp[1].split()))
selection(set)
sub = powerSet(set,int(inp[0]))
if sub:
    for i in sub:
        print(i)
else:
    print('No Subset')