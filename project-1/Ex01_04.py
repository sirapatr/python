print('*** Fun with Drawing ***')
n = int(input('Enter input : '))
s = n*4-3

coords = [['#' for x in range(s)] for y in range(s)]

for i in range(s):
    j = i
    while j<s-1-i :
        if(i%2 == 1):
            coords[i][j] = '.'
            coords[j][i] = '.'
        j += 1

    k=0
    while k <= i:
        if( k> s -i-2):
            if (i % 2 == 1):
                coords[i][k] = '.'
                coords[k][i] = '.'
        k+=1


for i in range(s):
    for j in range(s):
        print(coords[i][j], end='')
    print()