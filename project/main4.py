# n = input("введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("не целое")
#         n = input("введите целое число: ")
#
# if n % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")


# while True:
#     n = int(input("положительное число: "))
#     if n > 0:
#         break

# res = 1
# while True:
#     n = int(input(" введите число: "))
#     if n == 0:
#         print("результат:", res)
#         break
#     res = res * n

# i=0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("цикл окончен: i =", i)

# i = 1
# while i < 5:
#     print("внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tвложенный цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 20:
#         if i % 2 == 1:
#             print("+", end="")
#         else:
#             print("-", end="")
#
#         j += 1
#     print()
#     i += 1


# for element in collection:
#     print(element)

# i = 0
# for i in "red", "orange", "black":
#     print(i, "color =", i)

# range(start, stop, step)

# for i in range(9, 2, -1):
#     print(i, end=" ")

# n = int(input("введите целое число: "))
# for i in range(1, n//2+1):
#     if n % i == 0:
#         print(i, end=" ")


# for i in range(10, 101):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
#     else:
#         print("done")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")


# a = int(input("высота: "))
# b = int(input("Ширина: "))
# for i in range(a):
#
#     for j in range(b):
#
#         if i==0 or i == a-1 or j==0 or j == b-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# a = [letter * 2 for letter in "hello"]
# print(a)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# списки
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# num = [8, 3, 9, 4, 1, [1, 2, 3]]
# print(num)
# print(type(num))
# print("длина: ", len(num))
#
# s = []
# print(type(s))
# b = list("hello")
# print(b)

# s = [5, 1]*6
# print(s)

# n = list(range(10))
# print(n)
# n2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# if n is n2:
#     print("ravno")
# else:
#     print("raznoe")


# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)

# a = [1, 2, 3]
# b = [5, 6]
# c = b + a
# print(c)
# d = c * 2
# print(d)

# a = [0] * int(input("число: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)


# a = [int(input("->")) for i in range(int(input("кол элементов: ")))]
# print(a)

# a = [1, 5, 7, 6]
# for i in range(len(a)):
#     print(a[i], end=" ")
#
#
# for i in a:
#     print(i, end=" ")

# a = [0] * int(input("количество: "))
# res = 0
# for i in range(len(a)):
#     a[i] = int(input("->"))
#     if a[i] < 0:
#         res += a[i]
# print(res)


# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in n:
#     if i % 2:
#         s += i
#     else:
#         k += 1
# print("количество четных : ", k)
# print("сумма нечетных", s)


# a = [0] * 5
# k = s = 0
# for i in range(len(a)):
#     a[i] = int(input("число: "))
#     if a[i] != 0:
#         k += 1
#         s += a[i]
# print("среднее арифметическое:", s/k)


# a = [int(input("->")) for i in range(6)]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")


# a = [7, 8, 2, 1, 17]
# a[0], a[-1] = a[-1], a[0]
# print(a)

#
# a = [int(input("->")) for i in range(6)]
# for i in range(1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")


# срезы
# список[start:stop:step]


# s = [5, 9, 7, 5, 6]
# print(s[1:4])
# print(s[::2])
# print(s[::-1])
# print(s[-2:1:-1])


# s = [1, 2, 3, 4, 5, 6, 7, ]
# print(s)
# # print(s[:])
# # print(s[::-1])
# # print(s[::2])
# # print(s[1::2])
# # print(s[0:1])
# # print(s[-1:])
# # print(s[3:4])
# # print(s[])
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3] = [30]
# print(s)


# методы списка


# s = [1, 20, 35, 54, 2, 5, 7, 5, 4]
# print(s)
# s.append(99)
# print(s)
# s.extend([9, 8, 7]) # добавляет несколько элементов в конец списка
# print(s)
# s.extend('add')
# print(s)

# a = [i for i in range(1, 10)]
# s =[]
# for i in range(len(a)):
#     s.extend([i**2])
# print(s)
# s.insert(1, 100)# вставляет по индексу со сдвигом остальных в право
# print(s)

# s = []
# n = int(input("кол элем  списка: "))
# for num in range(n):
#     x = int(input("введите число: "))
#     s.append(x)
#     s.extend([x])
#     s.insert(-1, x)#в конце не получится вставить
#
# print(s)

# n = int(input("количество элементов списка: "))
# lst = []
# for i in range(n):
#     x = int(input("введите число кратное 3: "))
#     if x % 3 == 0:
#         lst.append(x)
#     else:
#         print("число не делится на 3 без остатка")
# print(lst)


# a = [5, 9, 4, 5, 6, 5, 4]
# b = [5, 6, 78, 45, 2, 4]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             if  i not in c:
#                 c.append(i)
# print(c)

# a = [5, 9, 4, 7, 8]
# b = [5, 6, 78]
# c = []
# if len(b) < len(a):
#     a, b = b, a
# for i in range(len(a)):
#    c.append(a[i])
#    c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

a = [5, 9, 4, 7, 8, 10, 15]
# a[4:] = []
# if 20 in a:
#     a.remove(20) #удаляет по значению первый попавшийся элемент
# print(a)
# a[2:6] = []
# last = a.pop()# удаляет последний элемент списка и записывает его в переменную(взвращает)
# print(last)
# print(a)
# second = a.pop(-2) #если есть число в скобках то удаляет по индексу
# print(a)
# print(second)
#s.clear() # очищает список
# del a[:]
# print(a)

n = int(input("введите количество элементов: "))
s = []
for i in range(n):
    s.append(int(input("->")))
k = int(input("введите индекс: "))
# del s[k]
s.pop(k)
print(s)




