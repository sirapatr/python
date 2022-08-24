def f(a=[]):
    print(a, end=" ")
    a.append(1)
    print(a)


for i in range(5):
    f()

f([2])
b = list(range(0, 10, 2))
print(b, len(b))

for i in range(-2, 13, 2):
    print(i,end=',')