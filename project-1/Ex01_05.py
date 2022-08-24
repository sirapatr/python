val = int(input('Enter Input : '))
size = (val+2)*2
for j in range(size):
    for i in range(size):
        w = (val - j + 1)<= i <= (val+1) or(val+2< i < size -1 and 0 < j < val + 1)
        b = (val + 1) < i <= (3*val + 5- j)
        if 0 < i < val+1 and val+2<j<size-1:
            print('+',end='')
        elif w:
            print('#',end='')
        elif b:
            print('+',end='')
        else:
            print('.',end='')
    print()