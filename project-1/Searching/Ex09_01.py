def bi_search(l, r, arr, x):
    if r == 1 and x != arr[l]:
        return False
    l = r//2
    if x > arr[l]:
        check = bi_search(0,r-l,arr[l:],x)
    elif x < arr[l]:
        check = bi_search(0,l, arr[:l], x)
    else:
        return True
    return check

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))