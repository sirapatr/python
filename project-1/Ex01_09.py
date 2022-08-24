def hbd(age):
    val = age//2
    if(age%2 == 1):
        return "saimai is just 21, in base %d!"%(val)
    else:
        return "saimai is just 20, in base %d!"%(val)



year = input("Enter year : ")

print(hbd(int(year)))