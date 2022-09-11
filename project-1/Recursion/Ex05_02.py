def list_sort(list,list2 = []):
    if len(list) == 0:
        return list2
    m = list.pop(0)
    return list_sort(list,isOver(list2, m))


def isOver(list, m, lo = 0):
    if lo == len(list):
        list.append(m)
        return list
    if list[lo] < m:
        list.insert(lo, m)
        return list
    return isOver(list, m, lo+1)

inp =list(map(lambda x:int(x),input('Enter your List : ').split(',')))
print('List after Sorted :',list_sort(inp))