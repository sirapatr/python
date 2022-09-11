def binary(val,val2,m = 0):
    if m < val2:
        bi = f'{m:0{val}b}'
        print(bi)
        return binary(val,val2,m+1)
    else:
        return

inp = int(input('Enter Number : '))
if inp < 0:
    print('Only Positive & Zero Number ! ! !')
else:
    binary(inp,2**inp)