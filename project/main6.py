# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# lst = [1, 2, 3, 4]
# print(change(lst))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5)
# print(is_greater(5, 10)


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch = "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
# p = input("введите пароль: ")
# if check_password(p):
#     print("надежный")
# else:
#     print("не надежный")


# def get_sum(a, b, c=0, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5, d=2))


# def sim(a=20, b="-"):
#     print(b*a)
#
#
# sim()


# def digit_sum(n, event=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if event and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not event and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
# print("Сумма четных цифр: ")
# print(digit_sum((9874023)))
# print(digit_sum((12358)))
# print(digit_sum((12596354754)))
# print("Сумма нечетных цифр: ")
# print(digit_sum(9874023, event=False))
# print(digit_sum(12358, event=False))
# print(digit_sum(12596354754, event=False))


# def display_info(name, age):
#     print("name:", name, "\nage", age)
#
# display_info("ira", 23)
# display_info(23, "ira")
# display_info(age=23, name="ira")
# display_info("igor",age=23, name="ira")#ошибка




# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1==lt2)
# print(lt1 is lt2)
#
# a = "hello"
# b = "hello"
# print(a==b)
# print(a is b)

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(id(lt1))
# print(id(lt1[1]))


# s = "hello"
# print(s)
# print(id(s))
# s+= "world"
# print(s)
# print(id(s))

# s = "hello"
# # s[1] = "a"
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))


#кортеж

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())# размер в памяти
# print(tpl.__sizeof__())

# a=1, 2, 3,3
# print(type(a))
# print(a)
# b = tuple()
# print(type(b))
#
# b = tuple((1, 2, 3, 4))
# print(type(b))
#
# c = tuple("hello")
# print(c)


# t = (1,)
# print(t)
# print(type(t))


# b = (1, 2, 3, 4, 5)
# print(b)
#
# print(b[3])
# print(b[1:3])
#
# b[1] = 3

# s = tuple(int(input("->")) for i in range(3))
# print(s)

# s = input("строка: ")
# a = tuple(s)
# print(a)

# from random import *
# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
#
#
# print(tuple(randint(0, 100) for i in range(10)))

# t = tuple(2**i for i in range(1, 12))
# print(t)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index("e"))
# for i in t3:
#     print(i, end=" ")


from random import *

# def flood():
#     a = tuple(randint(0, 6) for i in range(10))
#     b = tuple(randint(-5, 1) for i in range(10))
#     return a, b
#
# n, m = flood()
# print(n)
# print(m)
# nm = n + m
# print(nm)
# print(nm.count(0))



# def filter(a):
#     b = []
#     for i in a:
#         if i not in b:
#             b.insert(0, i)
#     b = tuple(b)
#     return b
#
# a = [2,3,1,0,3,5,9,5]
# print(filter(a))


# t = (1,2,3)
# x, y, z = t
#
# def get_user():
#     name = "tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)


# contries = (
#     ("германия", 80.2, (("берлин", 3.3), ("гамбург", 1.7))),
#     ("франция", 66, (("париж", 2.2), ("марсель", 1.6))),
# )
# print(contries)
# for country in contries:
#     # print(country)
#     countryName, countryPop, cities = country
#     print("\nстрана",countryName, "население =", countryPop, cities)
#     for city in cities:
#         # print(city)
#         cityName, cityPop = city
#         print("gorod", cityName, "naselenie", cityPop)



# множества (set)


# s = {"banana", "aple", "orange"}
# print(type(s))
# print(s)
#
# s = {x*x for x in range(10)}
# print(s)


# def to_set(element):
#     s = set(element)
#     return s, len(s)
#
#
#
# print(to_set("обычная строка"))
# print(to_set([5,6,2,5,6,2,85,9,6,2,5,6]))



# t = {"red","green","blue"}
# # print("green" not in t)
# for i in t:
#     print(i)



# r = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # a = {i for i in r if "a" not in i}
# # a = {"A"+i[1:] if i[0]=="a" else "B"+i[1:] for i in r}
# a = {"A"+i[1:] if i[0]=="a" else "B"+i[1:] for i in r if i[1] == "c"}
# print(a)





