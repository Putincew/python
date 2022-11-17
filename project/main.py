# name = "Andrey"
#
# print("Hello world!!!!", name)
# age = 20
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# a = b
# print(id(a))
# print(id(b))


# a = b = c = 1
# print(a,b,c)

# a, b, c = 5, "hello", 9.2
# print(a,b,c)

# _name_2 = "Bob"
# print(_name_2)
#
# import keyword
# keyword.kwlist

# PI = 3.14
# print(PI)


# name = Andrey
# age = 20
# print("меня зовут: " + name + "мне " + str(age) + "лет")
# print("меня зовут: ", name , "мне ", str(age), "лет")

# a = 1
# b = 2
# print("a: ", a)
# print("b: ", b)
# a, b = b, a
#
# print("a: ", a)
# print("b: ", b)

# s1 = "hello"
# s2 = "python"
# print(s1 + ", " + s2 + "!\t\t")
# print("*"*40)

# print(2.654654213456165435454)
#
# print(6/2)
# print(6//2)
# print(7/2)
# print(7//2)

# a = 4562
# b = a%1
# a = a//10
# c = a%10
# a = a//10
# d=a%10
# a = a//10
# e=a%10
# print(e*1000+d*100+c*10+b)


# num1 = "2"
# num2 = 3
# res = int(num1)+int(num2)
# print(res)
#
# print(int(3.8))
# print(round(3.896, 2))
#
# a=5/3
# print(round(a, 2))

#
# a='5.2'
# b=10
# c=int(float(a))+b
# print(c)
#
# a=1
# b=6
# print("a: ", a, "\nb: ", b)
# print("a: ", a)

# print("меня зовут", name, "мне", age, "лет", sep="", end=" ")
# print("меня зовут", name, "мне", age, "лет", end="\n\n")

# name = input("введите имя: ")
# city = input("ваш город: ")
# print(name, city)

# a = int(input("введите число: "))
# b = int(input("введите степень: "))
# print("число "+ str(a) + " в степени "+ str(b) + " = " + str(a**b))

# a=input("введите число: ")
# b=input("введите число: ")
# a = int(a)+int(b)
# c=input("введите число: ")
# d=input("введите число: ")
# b= int(c)+int(d)
# print("результат:", round(a/b, 2))

# a = True
# b = False
# print(a+5)
# print(b*5)
#
# print(bool("py"))

# print(bool(0.0))
# print(bool(None))
#
# test = None
# print(test)
# test = 5
# print(test)

# print("ghbdtn" <= "ghbdtn")


# print(4<6<9)

# print(not 9-7)
# print(not 9-9)


# cnt = 5
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("ваш возраст: "))
# if age >= 18:
#     print("разрешено")
# else:
#     print("запрещено")

# a=int(input("сторона 1: "))
# b=int(input("сторона 2: "))
# c=int(input("сторона 3: "))
#
# if a==b==c:
#     print("треугольник равносторонний")
# elif a==b or b==c or a==c:
#     print("треугольник равнобедренный")
# else:
#     print("треугольник разносторонний")


# day = int(input("введите день недели цифрой: "))
#
# if 1<=day<=5:
#     print("рабочий день - ", end="")
#     if  day==1:
#         print("пн")
#     if  day==2:
#     print("вт")
#     if  day==3:
#     print("ср")
#     if  day==4:
#     print("чт")
#     if  day==5:
#     print("пт")
# elif day == 6 or day == 7:
#     print("выходной день = ", end="")
#     if day == 6:
#         print("сб")
#     if day == 7:
#         print("вс")
#
# else:
#     print("Такого дня недели не существует")




#тернарное выражение

# a, b = 10, 20
# # minim = a if a < b else b
# print("a = b" if a==b else "a > b" if a > b else "b > a")

# a=1
# b=1
# print("на ноль делить нельзя" if b==0 else a / b)


# исключения

# try:
#     n = int(input("целое число: "))
#     print(n * 2)
# except ValueError:
#     print("что то не так")
#
# try:
#     n = int(input("делимое"))
#     m = int(input("делитель"))
#     print(n/m)
# except (ValueError, ZeroDivisionError):
#     print("нельзя делить строки")
# # except ZeroDivisionError:
#     print("нельзя делить на ноль")
# else: # когда в try не возникло исключения
#     print("все правильно")
# finally: # выполнение в любом случае
#     print("конец проги")

# n = input("введите целое числр: ")
# m = input("введите второе целое число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + str(m))


# i = 10
# while i > 0:
#     print("i = ", i)
#     i -= 1

# i = 0
# while i < 20 :
#     i += 2
#     print("i = ", i)

# a = int(input("количество символов: "))
# i = 0
# while i < a:
#     print("*", end="")
#     i += 1

n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
if n > m:
    n, m = m, n
summa = 0
while n <= m:
    if n % 2 == 1:
        summa += n
    n += 1
print("Сумма нечетных чисел диапозона:", summa)





