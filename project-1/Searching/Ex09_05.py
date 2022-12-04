inp = input('Enter Input : ').split('/')
size = int(inp[1])
data = list(map(int,inp[0].split()))

l = 0
r = 999999999
while l < r:
    mid = (l+r)//2
    box = 0
    val = 0
    for i in data:
        if i > mid:
            box = size +1
            break
        if val + i > mid:
            box += 1
            val = i
        else:
            val += i
    if box < size:
        r = mid
    else:
        l = mid + 1

print('Minimum weigth for',size,'box(es) =',l)