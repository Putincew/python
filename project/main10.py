# рекурсия

# def elevator(n):
#     if n==0:
#         print("вы в подвале")
#         return
#     print('=>', n)
#     elevator(n-1)
#     print(n, end=' ')
#
# n1 = int(input('этаж'))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return  res
#
# print(sum_list([1,2,3,5,7]))


# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0]
#     else:
#         print(lst, '=> lst[0]:', lst[0])
#
#         return lst[0] + sum_list(lst[1:])
#
# print(sum_list([1,2,3,5,7]))


# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(4000, 16))



# names = ['adam', ['bob', ['chet', 'cat'], 'bard', 'bert'], 'alex', ['bea', 'bill'], 'ann']
#
# print(type(names[0]) == str)
# print(type(names[0]) == list)
#
# print(isinstance(names[1], list))

# names = ['adam', ['bob', ['chet', 'cat'], 'bard', 'bert'], 'alex', ['bea', 'bill'], 'ann']
#
# def count(lst):
#     cnt = 0
#     for i in lst:
#         if isinstance(i, list):
#             cnt += count(i)
#         else:
#             cnt += 1
#
#     return cnt
#
# print(count(names))


#
# names = ['adam', ['bob', ['chet', 'cat'], 'bard', 'bert'], 'alex', ['bea', 'bill'], 'ann']
#
# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0] + union(s[1:]))
#     return s[:1] + union(s[1:])
#
# print('выпрямленный список:', union(names))


def remove(text):
    if not text:
        return ''
    if text[0] == '\t' or text[0] == ' ':
        return remove(text[1:])
    else:
        return text[0] + remove(text[1:])


print(remove('  hello\tworld   '))







































































































































































































































