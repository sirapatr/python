inp = list(map(int,input('Enter Input : ').split()))

for i in range(len(inp)-1,0,-1):
    x = None
    swap = False
    for j in range (i):
        if inp[j] > inp[j+1]:
            x = inp[j]
            inp[j],inp[j+1] = inp[j+1],inp[j]
            swap = True
    if not swap or i == 1:
        print('last step : ', inp, ' move[',x,']',sep='')
        break
    print(len(inp) - i, ' step : ', inp, ' move[', x,']',sep='')