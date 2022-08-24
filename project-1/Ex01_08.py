def oddEven():
    if value[0] == "S" :
        val = list(value[1])
        if value[2] == 'Even' :
            count = False
        else:
            count = True
        for i in range(len(val)) :
            if count :
                print(val[i] ,end='')
            count = not count


    else:
        val = value[1].split(' ')
        if value[2] == 'Odd':
            l = val[0::2]
            print(l)
        else :
            l = val[1::2]
            print(l)



print('*** Odd Even ***')
value = input('Enter Input : ').split(',')
oddEven()