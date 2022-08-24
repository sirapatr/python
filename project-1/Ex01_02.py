def windCheck():
    print('Wind classification is ',end='')
    if wind >=209:
        print('Super Typhoon.')
    elif wind >=102:
        print('Typhoon')
    elif wind >= 56:
        print('Tropical Storm.')
    else:
        print('Breeze.')

print(" *** Wind classification ***")
wind = float(input('Enter wind speed (km/h) : '))
windCheck()

