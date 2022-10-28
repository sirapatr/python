inp = list(map(int, input('Enter Input : ').split()))
arr = []
for i in inp:
    if i >= 0:
       arr.append(i)

for i in range(len(arr) - 1, 0, -1):
    x = None
    swap = False
    for j in range (i):
        if arr[j] > arr[j + 1]:
            x = arr[j]
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap = True
    if not swap:
        break

for i in range(len(inp)):
    if inp[i] < 0:
        arr.insert(i,inp[i])

for i in arr:
    print(i,end=' ')