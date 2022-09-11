def asteroid_collision(asts):
    #Code Here
    if len(asts) == 1:
        return asts
    res = asteroid_collision(asts[1:])

    if len(res) > 0 and res[0] < 0 and asts[0] > 0:
        if -res[0] > asts[0]:
            return res
        elif -res[0] < asts[0]:
            res.pop(0)
            res.insert(0,asts[0])
            return asteroid_collision(res)
        elif -res[0] == asts[0]:
            if len(res) > 1:
                return res[1:]
            else:
                return []

    else:
        res.insert(0,asts[0])
        return res

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))

