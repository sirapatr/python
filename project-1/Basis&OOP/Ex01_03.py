print(' *** Summation of each digit ***')
value = list(input('Enter a positive number : '))
Ans = 0
for i in value:
    Ans +=int(i)

print(f'Summation of each digit =  {Ans}')