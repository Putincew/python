# Задание 1

def count_minus(lst, res=0):
    if len(lst) == 1:
        if lst[0] >= 0:
            return res
        else:
            return res + 1
    else:
        if lst[0] < 0:
            res += 1
    return res + count_minus(lst[1:])
    

ls = [-2, 3, 8, -11, -4, 6]
print(count_minus(ls))




# Задание 2

def list_merge(lst):
    merge = []
    while lst:
        i = lst.pop(0)
        if isinstance(i, list):
            lst = i + lst
        else:
            merge.append(i)
    return merge
    
ls = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']

print(list_merge(ls))