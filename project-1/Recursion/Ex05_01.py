def Max(list, lo, m=0):
    if lo == len(list):
        return m
    if lo == 0:
        m = list[lo]
    if list[lo] > m:
        m = list[lo]
    return Max(list,lo+1,m)



inp =list(map(lambda x:int(x),input('Enter Input : ').split()))
print('Max : ',end='')
print(Max(inp,0))