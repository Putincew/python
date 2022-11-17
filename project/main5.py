# print(dir(list))
#
# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# num = s.count(0) # количество значений в списке
#
# index = s.index(0) # возврат индекса первого найденного в списке
# print(index)
#
#
# index = s.index(0, 3)
# print(index)


# a = [1,2,3]
# b = a
# s_copy = a.copy()
# a.append(20)
# print(a)
# print(b)
# print(s_copy)


# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# s.reverse() # не указывать в принте ничего не возвращает
# # print(list(s.revers()))
# print(s)

# s.sort()# разные типы данных списка не отсортирует
# print(s)
# s.sort(reverse=True)
# print(s)
#
# s2 = ["сергей", "виталий", "анна"]
# s2.sort()#алфавит первых букв
# print(s2)
# s2.sort(key=len)# сортировка по длине. что делать с каждым элементом
# print(s2)

# str = sorted(s) # не меняет список, возвращает отсортированный. работает с разными типами, универсальная
# print(str)


# генерация случайных данных

import random as r  # нажать с ctrl посмотреть модержимое. ас даем псевдоним
from random import *

# print(random.random())
# print(randint(0, 9))
# print(randrange(0, 10, 2))
# print(round(uniform(10.5, 25.5), 2))
#
# s = [55,66,77,88,99,30,40,76,53]
# print(choice(s))
# print(choices(s, k=5))
#
# shuffle(s)
# print(s)
#
#
# mas = [randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(sum(lst))# только с числами
# print(min(lst))# по алфавиту
# print(max(lst))


# s = [71,19,22,88,27,52,50,57,10,19]
# n = s.pop((s.index(max(s))))
# s.insert(0, n)
# print(s)


#
# s = [randint(-20,20) for i in range(10)]
# s.sort(reverse=True)
# print(s)

# s = [randint(-20,20) for i in range(10)]
# print(s)
# n = s.index(min(s))
# print(s[n])
# del(s[n-1])
# print(s)

# x = list('1a2c2f2gh')
# print(x)
# print('a' in x)
#
# lst = []
# if not lst:
#     print('пусто')

# s = [randint(0, 10) for i in range(int(input("размер первого списка ")))]
# t = [randint(0, 10) for i in range(int(input("размер второго списка ")))]
# u = s + t
# print(s)
# print(t)
# # print(u)
#
# u = []
#
# for i in s:
#     if i in t and i not in u:
#         u.append(i)
# print(u)

# k = int(input("размер списка "))
# s = []
# while len(s) < k:
#     n = randint(1, k)
#     if n not in s:
#         s.append(n)
# print(s)


# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# print(m[0])


# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11]
# ]
# n = [[x**2 for x in row] for row in m]
# for i in m:
#     for x in i:
#         print(x, end="\t")
#     print()
# print(*n, sep="\n")

# w = (int(input("ширина: ")))
# h = (int(input("высота: ")))
# m = [[0 for x in range(w)] for i in range(h)]
# for i in m:
#     for x in i:
#         print(x, end="\t")
#     print()


# for x, y in [[1,2], [3,4], [5,6], [7,8]]:
#     print(x, "+", y, "=", x+y)

# w, h = 5 , 4
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# col = 0
# for i in matrix:
#     for x in i:
#         print(x, end="\t")
#         if x < 0:
#             col += 1
#     print()
# print("количество отрицательных значений",col)


# w, h = 3 , 4
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# col = 1
# for i in matrix:
#     for x in i:
#         print(x, end="\t")
#         if x != 0:
#             col *= x
#     print()
# print("произведение не нулевыхЖ ",col)



# w, h = 6 , 6
# matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
# for i in matrix:
#     for x in i:
#         print(x, end="\t")
#
#     print()
# print()
# for i in range(len(matrix)):
#     if i % 2 == 0:
#         for x in range(len(matrix[i])):
#             print(matrix[i+1][x], end="\t")
#     else:
#         for x in range(len(matrix[i])):
#             print(matrix[i-1][x], end = "\t")
#
#     print()



# import math
#
# print(dir(math))
#
# num1 = math.sqrt(2)
#
# num2 = math.ceil(3.2)
#
# num3 = math.floor(3.8)
#
# print(math.pi)


import time
#
# second = time.time()
# print(second)
# localtime = time.ctime()
# print(localtime)
#
# res = time.localtime(second)
# print(res)
# print(res.tm_year)
#
#
# print(time.strftime("today is %B %d,%Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(7999999587)))



# pause = 5
# print("start...")
# time.sleep(pause)
# print(pause, "second.")


# test = input("название напоминания: ")
# local_time = float(input("через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(test)


# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime("сегодня %B %d,%Y"))



# def hello(name, word):
#     print("say", "Hello", name)
#
#
# hello("irina", "hi")
# hello("ivan", "hello")


# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(2, 5)
#
# n = 2
# m = 5
# get_sum(n, m)


# def symbol(count, a, b):
#     print((a + b) * count)
#
#
# symbol(9, '+', '-')
# symbol(7, 'x', '0')

# def get_sum(a, b):
#     return a + b
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
# print(maximum(9, 16))


# def maximum(one, two):
#     if one > two:
#         return one - two
#     else:
#         return two + two
# print(maximum(int(input("первое число: ")), int(input("второе число: "))))