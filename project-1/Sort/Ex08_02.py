def selection(l):
    for last in range(len(l)-1,0,-1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1,last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last],l[biggest_i] = l[biggest_i],l[last]

inp = list(map(int, input('Enter Input : ').split()))
arr = []
for i in inp:
    if i >= 0:
       arr.append(i)

selection(arr)

for i in range(len(inp)):
    if inp[i] < 0:
        arr.insert(i,inp[i])

for i in arr:
    print(i,end=' ')