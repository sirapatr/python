def insertion(arr,data,l,lo):
    if not l:
        l.insert(0,data)
        return l
    if l[lo] <= data:
        l.insert(lo+1,data)
        print('insert',data,'at index',lo+1,':',l,end=' ')
        if len(l) == len(arr):
            print()
        else:
            print(arr[len(l):])
        return l
    elif lo == -1:
        l.insert(0,data)
        print('insert', data, 'at index', lo + 1, ':', l, end=' ')
        if len(l) == len(arr):
            print()
        else:
            print(arr[len(l):])
    else:
        l = insertion(arr,data,l,lo-1)
    return l


inp = list(map(int, input('Enter Input : ').split()))
l = []
for i in inp:
    l = insertion(inp,i,l,len(l)-1)

print('sorted')
print(l)