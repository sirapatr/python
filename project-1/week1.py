def e_base_basic(num):
    a = 0
    val = []
    for i in range (9,1,-1):
        if num % i == 0:
            a = i
            break

    if a == 0:
        a = 7

    while num > 0:
        val.insert(0,num%a)
        num //= a
    stri = ''.join(map(str, val))
    return int(stri)

inp = input('Enter Input : ')
print(e_base_basic(int(inp)))