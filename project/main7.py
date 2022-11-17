# a = {0,1,2,3}
# a.add('ann')
# print(a)
# a.remove(2)
# print(a)
#
#
# a.discard(2)
# print(a)
# a.pop()
# print(a)

a = {0, 1, 2, 3}
b = {1, 2, 3, 4}
# c = a.union(b)
# c = a|b
# print(c)
# a.update(b)
# a|=b
# print(a)
# c=a&b
# print(c)
# a &= b
# print(a)
# c = a - b
# print(c)
# c = a ^ b
# print(c)

# s1 = {1,2}
# s2 = {3}
# s3 = {4,5}
# s4 = {3,2,6}
# s5 = {6}
# s6 = {7,8}
# s7 = {9,8}
# # s = s1.union(s2,s3,s4,s5,s6,s7)
# s = s1 | s2 | s3 | s4|s5|s6|s7
# print(s)
# print(len(s))
# print(max(s))

# s1 = "hello"
# s2 = "how are you"
# s = set(s1) & set(s2)
# print(s)

# s1 = "Python"
# s2 = "Programming langueq"
# s = set(s1) - set(s2)
# print(s)


# draw = {"marina","jenya","sveta"}
# mus = {"kostya","jenya","ilya"}
# print('odno hobbi ',draw^mus)
# print('dva hobbi ',draw&mus)

# s = frozenset([1,2,3,4,5])
# print(s)


# словари

# s = ['one', 'two']
# print(s)
# d = {'one': 1, 'two': 2}
# print(d)

# d = {'one': 1, 'two': 2}
# print(type(d))
# print(d)

# a = [[1,2],[3,4],[5,6]]
# d = dict(a)
# print(d)

# d = {a: a**2 for a in range(1,7)}
# print(d)
# print(d[2])

# d = {0:'text', "one": 45, (1,2.3): 'kortej', 42: [2,3,4], True: 1}
# print(d)
# print('one' in d)
# print(d.keys())
# if 'one' in d:
#     print("true")
key = "four"


# if key in d:
#     del d[key]

# try:
#     del d[key]
# except KeyError:
#     print("'элемента с ключом"+str(key) + " нет в словаре")
#
# print(d)

# d = {0:'text', "one": 45, (1,2.3): 'kortej', 42: [2,3,4], True: 1}
# print(d)
#
# for key in d:
#     print(key, d[key])

# s = {'x1':3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for i in s:
#     res = s[i]*res
# print(res)

# d = {a: input("->") for a in range(1,5)}
# print(d)
# del d[int(input("исключить: "))]
# print(d)


# capitals = dict()
# capitals["rossiya"] = "Moskva"
# capitals["italia"] = "rim"
# capitals["ispania"] = "madrid"
#
# countries = ["rossiya", "italia", "francia", "ispania"]
#
# for country in countries:
#     if country in capitals:
#         print("stolica strany "+country+": "+ capitals[country])
#     else:
#         print("v base net strany "+country)


# goods = {
#     1: ['core-i3-4330', 9, 4500],
#     2: ['core-i5-4670K', 3, 8500],
#     3: ['AMD FX-6300', 6, 3700],
#     4: ['pentium', 8, 2100],
#     5: ['core-i5-3450', 5, 4600],
# }
#
# for i in goods:
#     print(i, ') ',goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб.", sep="")
#
# while True:
#     n = int(input("№: "))
#     if n != 0:
#         cnt = int(input("количество: "))
#         goods[n][1] = cnt
#     else:
#         break
# for i in goods:
#     print(i, ') ',goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб.", sep="")


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('e', 'False') #возв если нет ключа в словаре
# print(value)

# print(d)
# item = d.items()
# print(item)
# key = d.keys()
# print(key)
# value = d.values()
# print(value)
#
# for i in d:
#     print(i)
#
# for i in d.values():
#     print(i)
#
# for i, j in d.items():
#     print(i, '->', 'j')


# d = {'a': 1, 'b': 2, 'c': 3}
# d.clear()
# item=d.pop('b', 5)
# print(item)
# it = d.popitem()
# print(it)

# item = d.setdefault('e', 5)
# print(item)

# d.update([('a', 7), ('q', 9)])
#
# print(d)

# d2 = d.copy()
#
# print(d)
# print(d2)
# d['e'] = 7
# print(d)
# print(d2)


#
# a = {'a': 1, 'b': 2, 'c': 3}
# b = {'b': 3, 'c': 3}
# # c = a.copy()
# # c.update(b)
# # c = a | b
# # print(c)
#
# d = {'name': ' kelli', 'age': 25, 'salary': 8000, 'city': 'newYork'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# d['location'] = d.pop('city')

# print(d)
# print(new_d)

# d = {'один': 1, 'dva': 2, 'tri': 3, 'chetyre': 4}
# a = dict()
# a = {key: value for key, value in d.items() if len(a)<=2}
# print(a)

# value = int(input('->'))
# lt = [1,2,3,4,5]
# a = {i: value for  i in lt}
# print(a)
# a = {i: 'value' for i in range(1,9)}
# print(a)
# d = dict.fromkeys(['a','b'], 100)
# print(d)


# figures = {1: 'rect', 2: 'try', 3: 'circ'}
# value = list(figures.items())
# print(value)

# a = ['one', 1,2,3,'two',10,20,'three',15,36,60,'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i # 'one'
#     else:
#         d[s].append(i)
# print(d)

# zip

# d = dict(zip([1,2,3], ['dec', 'jan', 'feb']))
# print(d)

# a = [1,2,3]
# print(list(zip(a)))
# print(list(zip(range(5), range(100))))

# a = {'name': ' igor', 'lastName': 'smit', 'job': 'cons'}
# b = {'name': ' irina', 'lastName': 'doe', 'job': 'manage'}
#
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)


# a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# x, y = zip(*a)
# print(x)
# print(y)
# l1 =[2, 1, 3, 4]
# l2 = ['b', 'a', 'c', 'd']
# a1 = list(zip(l1, l2))
# print(a1)
# a1.sort()
# print(a1)

# month = ['jan', 'fab', 'mar']
# tot_sales = [52000.00,51000.00,48000.00]
# prod_cost = [46800.00,45900.00, 43200.00]
# for t,p,m in zip(tot_sales,prod_cost,month):
#     res = t - p
#     print('чистая прибыль в ', m, '=', res)

# one = {'aple': 0.4, 'orange': 0.35}
# two = {'peper': 0.2, 'onion': 0.55}
# print({**one, **two}) #{'aple': 0.4, 'orange': 0.35, 'peper': 0.2, 'onion': 0.55}
#
# for k,v in {**one, **two}.items():
#     print(k, '->', v)

#
# en = [2, 5, 3, 4, 1, 5]
# j = 1
# for i in en:
#     print(j, '-й цвет: ', i, sep='')
#     j += 1
#
#
# en = [2, 5, 3, 4, 1, 5]
# j = 1
# for j, i in enumerate(en, 1):
#     print(j, '-й цвет: ', i, sep='')
#     j += 1


#
# en = {0: 1, 1: 2, 2: 3}
# for i, j in enumerate(en):
#     print(i, ': ', j, '->', en[j], sep='')
#
# a = [1,2,3]
# b = [*a,4,5,6]
# print(b)

# def func(*args):
#     return args
#
# print(func(1))
# print(func(1,2,3,'abc'))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
# num1 = summa(1,2,3,4,5,6,7,8,)
# num2 = summa(6,7,8,)
# print(num1)
# print(num2)

#
# def to_dict(*args):
#     d = {}
#     for i in args:
#         d[i] = i
#     return d
#
#
# print(to_dict(1,2,3,4))
# print(to_dict('gray', (2,17), 3.11, -4))

# def func(*num):
#     lst = []
#     a = sum(num) / len(num)
#     for i in num:
#         if i < a:
#             lst.append(i)
#     print(a)
#     return lst
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func(3, 6, 1, 9, 5))


# def func(a, *args):
#     return  a, args
#
# print(func(1))
# print(func(1,2,3, 'abc'))


# def print_scores(stud, *scores):
#     print('Student name: ', stud)
#     for score in scores:
#         print(score, end=' ')
#     print()
#
#
# print_scores('Jonatan', 100, 95, 88, 92, 99)
# print_scores('Rick', 96,20,33)


# def func(*args):
#     res = []
#     for i in args:
#         res.append(int(str(i)[::-1]))
#     return res
#
# print(func(12,2345,323,4456,5687,62,734,81,91))


# def reverse(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):
#             res.append(reverse(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))


# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))

# def info(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print('*' * 20)
#
#
# info(first_name='irina', last_name='petrova', age=22, phone=12345678)
# info(first_name='irina', last_name='petrova', age=22, phone=12345678, email='igor@gmail.com', country='russia')



# def db(**kwargs):
#     my_dict.update(kwargs)
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='bob', age=31, weight=61, eyes_color='gray')
# print('my_dict =', my_dict)





# def func1(*args):
#     print(args[0])
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1,2,3)
# func2(one=123, two=456)



# def func(a, *args, onr=True, **kwargs):
#     return a, args, kwargs
#
# print(func(5,9,7,8,6,one=False, b=2, c=3, d=4))



# Область видимости (scope)

# for i in range(5):
#     a= 5
#     print(i)
# print('i за пределами цикла',i)
# print('a за пределами цикла',a)


# name = 'tom'
#
# def hi():
#     print('hello', name)
#
#
# def bye():
#     global name
#     global surname
#     surname = 'ivanov'
#     name = 'bob'
#     print('good bye', name)
#
#
# hi()
# bye()
# print(name)
# print(surname)





# i = 5
#
# def func(arg=i):
#     print(arg)
#
# i=6
# func()




# def add_two(a):
#     x = 2
#     return  a + x
#
# print(add_two(3))
# print(x)



# def func(a):
#     x = 2
#
#     def inner():
#         print(x)
#         return a + x
#
#     return inner()
#
# print(func(5))



# max = [1,2,3,4,5]
# print(max(max))

# import builtins
#
# print(dir(builtins))


# вложенные функции

# def outer_func(who):
#     def inner_func():
#         print("hello", who)
#     inner_func()
#
# outer_func('world')


# def func1():
#     a = 6
#
#     def func2(b):
#         a = 4
#         print('summa: ',a + b)
#
#     print('a: ', a)
#     func2(4)
#
#
# func1()


# x = 25
# t = 0
#
#
# def fn():
#     global  t
#     a = 30
#
#     print("global", x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('nonlocal', a)
#
#     inner()
#     print(a)
#     t = a
#
#
# fn()
# z = x + t
# print(z)



# def fn1():
#     # x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x', x)
#
#     fn2()
#     print('fn1.x', x)
#
#
# fn1()


# def outer(a1,b1,a2,b2):
#     a = 0
#     b=0
#
#     def inner():
#         nonlocal a,b
#         a = a1 +a2
#         b = b1 + b2
#
#     inner()
#     return [a,b]
#
#
# res = outer(2,3,-1,4)
# print(res)


#
#
# def increment(number):
#     def inner():
#         return number +1
#     return inner()
#
#
# print(increment(10))


# замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# res = outer(5)
# print(res(10))
#
# print(res(2))
#
# res2 = outer(7)
# print(res2(5))
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1,2,3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a,b,c
#
#     return func2
#
# func = func1()
# print(func())



# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('moskow')
# res1()
# res1()
#
# res2 = func('sochi')
# res2()
# res2()
# res2()
#
# res1()



# students = {
#     'alice': 100,
#     'bob': 67,
#     'chris': 85,
#     'dsvid': 75,
#     'elise': 54,
#     'fiona': 35,
#     'grace': 69
# }
#
# def make_classifier(lower, upper):
#     def classifier_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classifier_student
#
#
# A = make_classifier(90, 101)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))




def func(a,b):
    def add():
        return a + b

    def sub():
        return a - b

    def mul():
        return a * b

    def replace():
        pass

    replace.add = add
    replace.sub = sub
    replace.mul = mul
    return replace


obj1 = func(5,2)
print(obj1.add())

print(obj1.sub())
print(obj1.mul())




















