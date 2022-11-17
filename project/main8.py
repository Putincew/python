# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x**2 + y**2)(5, 6))
#
# summ = lambda  a=1, b=2, c=3: a + b + c
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))


# func1 = lambda *args: args
#
# print(func1(1,2,3))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc_"))

# def inc(n):
#     return lambda x: x + n
#
# f = inc(42)
# print(f(3))
#
# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
# f1 = inc1(42)
# print(f1(3))
#
#
#
# inc2 = (lambda n: (lambda x: x + n))
# f2 = inc2(42)
# print(f2(3))
# print(inc2(42)(3))
#
# print((lambda n: (lambda x: x + n))(42)(3))

#
# inc = (lambda x: lambda y: lambda z: x + y + z)
# print(inc(2)(4)(5))

# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1], reverse=True)
# print(lst)
# dict1 = dict(lst)
# print(dict1)


# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['raiting'])
# print(res)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x*y), (lambda x, y: x / y)]
# b = a[2](12, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#     1: (lambda: print('понедельник')),
#     2: (lambda: print('вторник')),
#     3: (lambda: print('среда')),
#     4: (lambda: print('четверг')),
#     5: (lambda: print('пятница')),
#     6: (lambda: print('суббота')),
#     7: (lambda: print('воскресенье')),
# }
#
# d[5]()


# maximum = (lambda a, b: a if a > b else b)
# print(maximum(15, 13))

# minimum = (lambda a, b, c: a if b>a<c else b if  a>b<c else c)
# print(minimum(4, 5, 8))


# функция map()

# def multiple(t):
#     return t*2
#
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(multiple, lst)))
# print(list(map(lambda t: t * 2, lst)))


# t = 2.88, -1.75, 100.55
#
# print(tuple(map(lambda x: str(x), t)))
#
#
# a = ['2.88', '-1.75', '100.55']
# print(list(map(float, a)))


# areas = [3.4567854, 5.5679904, 7.456897, 56.5679534, 9.345789, 32.5467893]
# print(list(map(round, areas, range(1,7))))
# print(round(map(areas)))
#
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# lst = list(map(lambda x, y: (x, y), st, num))
# print(lst)
# tp = dict(lst)
# print(tp)

# l1 = [1,2,3]
# l2 = [4,5,6]
# print(list(map(lambda x, y: x + y, l1, l2)))


# filter(func, iterable)


# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda  s: len(s) == 3, t))
# print(t2)

# b = [65, 56, 34, 57, 37, 24, 54, 35]
# res = list(filter(lambda s: s > 33, b))
# print(res)

from random import *

# b = [randint(1, 40) for i in range(10)]
# print(b)
# res = list(filter(lambda s: 10 < s < 20, b))
# print(res)

# b = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda s: s % 15 == 0, b))
# print(res)


# декораторы

# def hello():
#     return "hello, i am func 'hello'"
#
# def super_func(func):
#     print("hello, i am func 'super_func'")
#     print(func())
#
#
# super_func(hello)
#
# test = hello
# print(test())


# def my_decorator(func):
#     def wrap():
#         print('code before')
#         func()
#         print('code after')
#     return wrap
#
# def func_test():
#     print("hello, i am func 'func_test")
#
#
# test = my_decorator(func_test)
# test()



# def my_decorator(func): # декорирующая функция
#     def wrap():
#         print('code before')
#         func()
#         print('code after')
#     return wrap
#
#
# @my_decorator # декоратор
# def func_test(): #декорируемая функция
#     print("hello, i am func 'func_test")
#
#
# @my_decorator # декоратор
# def hello(): #декорируемая функция
#     print("hello, i am func 'func_test")
#
# func_test()
# print()
# hello()



# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return 'text'
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('вызов:', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('hello')
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print('*'*50)
#         fn(arg1, arg2)
#         print('*'*50)
#
#
#     return wrap
#
# @args_decorator
# def print_full_name(first, last):
#     print('меня зовут', first, last)
#
#
# print_full_name('ирина', "лаврова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print('*'*50)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         print('*'*50)
#
#
#
#     return wrap
#
# @args_decorator
# def print_full_name(a, b, c, study='python'):
#     print(a, b, c, 'изучают', study, end='\n\n')
#
#
# @args_decorator
# def hello():
#     print('hello')
#
#
#
#
# print_full_name('ирина', "борис", "светлана", study="javascript")
# print()
# print_full_name('владимир', "екатерина", "виктор")
# print()
# hello()



# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=' ')
#             fn(x,y)
#
#         return wrap
#     return args_dec
#
# @decor('сумма:', '+')
# def summa(a, b):
#     print(a + b)
#
# @decor("разность:", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5,2)
# sub(5,2)



# def multiply(num1):
#     def umn(fn):
#         def wrap(num2):
#             return num1*num2
#
#         return wrap
#     return umn
#
# @multiply(3)
# def pro(num2):
#     return num2
#
# print(pro(4))



def typed(*args, **kwargs):
    def wrapper(fn):
        def wrap(*f_args, **f_kwargs):

            for i in range(len(args)):
                if type(f_args[i]) != args[i]:
                    raise TypeError('некорректный тип данных')
            for k in kwargs:
                if type(f_kwargs[k]) != kwargs[k]:
                    raise TypeError('некорректный тип данных')
            return fn(*f_args, **f_kwargs)
        return wrap
    return wrapper


@typed(int, int, int)
def typed_fn(x,y,z):
    return x*y*z

@typed(str, str, str)
def typed_fn2(x,y,z):
    return x+y+z

@typed(str, str, z=int)
def typed_fn3(x,y,z='hello!'):
    return (x+y)*z

print(typed_fn(3,4,5))
# print(typed_fn(3,4,'dodge'))
print(typed_fn2('hello','world', '!'))
print(typed_fn3('hello','world', z=5))

























































