def FirstGreater (arr,data):
    check = False
    for i in arr:
        if i > data:
            check = i
            break
    for i in arr:
        if i < check and i > data:
            check = i

    if not check:
        return 'No First Greater Value'
    else:
        return check


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in k:
    print(FirstGreater(arr,i))