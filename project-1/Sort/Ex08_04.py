def whereischar (data):
    var = list(data)
    for i in var:
        i = ord(i)
        if i - 48 > 9:
            return i

def selection(l,arr):
    for last in range(len(l)-1,0,-1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1,last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last],l[biggest_i] = l[biggest_i],l[last]
        arr[last],arr[biggest_i] = arr[biggest_i],arr[last]

inp = input('Enter Input : ').split()
li = []
for i in inp:
    li.append(whereischar(i))
selection(li,inp)
for i in inp:
    print(i,end=' ')
print()