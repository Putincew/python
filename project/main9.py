

# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end='')
#             fn(*args)
#
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
#
#
# @decor
# def hello_world(text):
#     print(text)
#
# @decor(decor_text='hello')
# def hello_world2(text):
#     print(text)
#
# hello_world('hi')
# hello_world2('world!')





# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))
# print(int('100', 10))

#
# print(bin(18))
# print(oct(18))
# print(hex(18))
#
# print(0b100 + 2)
# print(0o20 + 4)
# print(0x11 + 3)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * -3)
# print('y' in e)
# print(e[::-1])
# # e[3] = 't'
# e = e[:3] + 't' + e[4:]
# print(e)


# def change_char(s, c_old, c_new):
#     s2 = ''
#     for i in s:
#         if i == c_old:
#             s2 += c_new
#         else:
#             s2 += i
#
#     return s2
#
# st = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
# st2 = change_char(st, 'N', 'P')
# print('st1 =', st)
# print('st2 =', st2)



# print(u'Привет')
# print(r'C:\file.txt') #сырые строки. Игнорируют спецсимволы
# print(r'C:\file.txt\\'[:-1]) # в конце не должно быть слеша
# print(r'C:\file.txt' + '\\')
# name = 'Дмитрий'
# age = 20
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет')
# print(f'Меня зовут {name}. Мне {age} лет')
# print(f'{2.321354}')
# print(f'{round(2.321354, 2)}')
# print(f'{2.321354:.2f}')

# x = 10
# y = 5
# print(f'{x} x {y} / 2 = {x * y / 2}'
#       f' - выражение')

# d = 74
# print(f'{{{d}}}')


# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')



# """<div>
# <a href='#'>content</a>
# </div>
# """
#
# s = """<div>
# <a href='#'>content</a>
# </div>
# """
# "привет"
# print(s)

# def square(n):
#
#     """Принимает число n, возвращает квадрат числа n"""
#     a = 5
#     return n * 2
#
# print(square(5))
# print(square.__doc__)
# print(min.__doc__)


#
# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))


# print(ord('a'))
# print(ord('p'))
#
# while True:
#     n = input('->')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break


# mystr = 'test string for me'
# arr = [ord(x) for x in mystr]
# print(arr)
# arr = [int(sum(arr)/len(arr))] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in (input('->')[:3])] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(ar[-1]) - 1)


# print(chr(97))

# a, b = 122, 97
# if a > b:
#     a, b = b, a
#
# res = [chr(x) for x in range(a, b + 1)]
# res.sort()
# print(*res)



# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord('a'))
# print(ord('A'))


# from random import randint
#
# SHORTEST = 7
# LONGTEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def random_password():
#     random_length = randint(SHORTEST, LONGTEST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print('ваш случайный пароль: ', random_password())




# print(dir(str))

# s = 'hello, WORLD I am learning Python.'
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
#
#
# print(s.count('l', 3)) # количество вхождений подстроки в строку с заданного индекса
# print(s.find('Python', 4)) # с какого индекса начинается первая найденная подстрока с заданного индекса. возврат -1 если не найдено


# a = 'один два'
# b = a[:a.find(' ')]
# c = a[a.find(' ')+1:]
# print(b)
# print(c)
# print(c + ' ' + b)


# s = 'ab12c59p7dq'
# digits = []
#
# # for i in s:
# #     if i in '1234567890':
# #         digits.append(i)
# # print(digits)
#
#
# for i in s:
#     if '1234567890'.find(i) != -1:
#         digits.append(i)
# print(digits)

# s = 'hello, WORLD I am learning Python.'
# print(s)
# print(s.index('Python'))# с какого индекса начинается первая найденная подстрока с заданного индекса. возврат ошибка
#
# print(s.rfind('l'))
# print(s.rindex('l'))

#
# s = 'I am learning Python, hello, WORLD!'
#
# first = s.find('h')
# fin = s.rfind('h')+1
#
# print(s[:first] + s[fin:])


# print('abc123'.isalnum())# определяет состоит ли строка из цифр или букв
# print('ф'.isalpha())# определяет состоит ли строка из букв
# print('123'.isdigit())# определяет состоит ли строка из цифр
# print('abc2'.islower())# определяет состоит ли строка из строчных букв без учета цифр
# print('ABC2'.isupper())# определяет состоит ли строка из заглавных букв без учета цифр




# print('py'.center(10, '-'))#выравнивание строки  по центру
# print('py'.center(30, '*'))

# print('    py'.lstrip())
# print('    py     '.rstrip())
# print('    py     '.strip())# удаляет пробелы или указанные в скобках символы. Выше слева или справа
#
# print('https://www.python.org'.lstrip('/:pths'))# удаляет перечисленные числа только подряд
# print('py.$$$;'.rstrip(';$.'))
# print('https://www.python.org'.lstrip('/:pths').rstrip('org.'))


# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(st)
# print(st.replace('Nython', 'Python'))


# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print('..'.join(['1', '2'])) # обьединяет массив, список, кортеж, строку в одну строку через символ разделитель
#
# print(':'.join('hello'))


# print('строка разделенная пробелами'.split()) # делит строку на список из подстрок
# print('строка_разделенная_пробелами'.split('_'))
# print('строка разделенная пробелами'.split('а'))
#
# print('www.python.org.ru'.split('.', 5))


# a = list(map(int, input('->').split()))
# print(a)
#
# fio = input('введите ФИО: ').split()
# print(fio[0], ' ', fio[1][0] + '.', fio[2][0] + '.', sep='')

# print('www.python.org.ru'.split('.', 5))
# print('www.python.org.ru'.rsplit('.', 1))
# print('www...python...org...ru'.split('.'))
# print('...'.split('.'))

# s = 'В строке пробел заменить на звездочку'.split()
# print('*'.join(s))





# регулярные выражения


import re


# s = 'Я ищу совпадения в 2023 году. И я найду их в 2 счёта.'
# reg = r'\.'

# print(s.find(reg))
# print(re.findall(reg, s)) # ['я', 'я']
# print(re.findall('12', s)) #[]
#
# print(re.search(reg, s)) # месторасположение первого совпадения обьекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.match(reg, s)) # поиск по шаблону в начале строки

# print(re.split(reg, s)) # возвращает список, в котором строка разбита по шаблону
# print(re.split(reg, s, 1))

# print(re.sub(reg, '!' ,s, 1)) # заеняет совпадения на указанный символ


# s = 'Я ищу совпадения в 2023 году. И я найду их в 2 счёта. 9578'
# # reg = r'[12][09][0-9][0-9]'
# reg = r'[А-яё.]'
#
# print(re.findall(reg, s))



# s1 = 'Ели[-ели].'
# pattern = r'[А-яё.\[\]-]'
# print(re.findall(pattern, s1))

# s2 = 'Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09.'
# pat = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(pat, s2))



# s = 'Я ищу совпадения в 2023 году. И я найду их в 2 счёта. 9578 19_45'
# # reg = r'[^0-9]'
# reg = r'\s'
#
# print(re.findall(reg, s))


#повтор
#+ от 1 до бесконечност
#* - от 0 до бесконечности
#? - 0 или 1
#

# s = 'Я ищу совпадения в 2023 году. И я найду их в 2 счёта. 9578 19_45'
# # reg = r'[^0-9]'
# reg = r'\A\w\s\w'# в начале строки
# reg = r'\w\s\w\Z'#в конце строки
# reg = r'\b\w\s\w' #в начале слова
# reg = r'\w\s\w\b' #в конце слова
# reg = r'\B\w\s\w'#везде кроме начала слова
# reg = r'0*'
#
#
#
# print(re.findall(reg, s))




# s1 = 'Цифры: 7, +17, -42, 0013, 0.3'
# pattern = r'\d+'
#
# print(re.findall(pattern, s1))


# s1 = '05-03-1987 # Дата рождения'
# # pattern = r'\d+'
# #
# print('дата', re.sub(r'#.*', '', s1))
# print('дата', re.sub(r'-', '.', re.sub(r'#.*', '', s1)))


# s1 = 'autor=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# pattern = r'\w+\s*=[^;]+'
# print(re.findall(pattern, s1))


# s1 = '12 сентября 2021 года'
# pattern = r'\d{2,4}'
# print(re.findall(pattern, s1))


# s1 = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# pattern = r'\+?7\d{10}'
# print(re.findall(pattern, s1))

#
# s1 = 'Я ищу совпадения в 2023 году. И я найду их в 2 счёта. 9578 19_45'
# pattern = r'^\w+\s\w+'
# pattern = r'\w+\s\w+$'
# print(re.findall(pattern, s1))


# def login(a):
#     return re.findall(r'^[\w!@#$-]{8,25}$', a)
#
# print(login('admin_admin'))
# print(login('admin_admin*'))



# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))
# print(re.findall(r'[я]', 'Я я', re.IGNORECASE))
# print(re.findall(r'[я]', 'Я я', re.IGNORECASE))


# text = """
# one
# two
# """
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))



# text = """
# one
# two
# """
# print(re.findall(r'one$', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))

#
# print(re.findall('''
# [A-z.-]+ # part 1
# @        # поиск символа @
# [a-z_.-]+# part 2
# ''', 'test@mail.ru', re.VERBOSE))


# text = 'hello. world'
# print(re.findall(r'\w\+', text, re.DEBUG))

# text = '''Python,
# python,
# PYTHON'''
# reg = '(?mi)^python'
# print(re.findall(reg, text)) #flags=re.IGNORECASE | re.MULTILINE))



# s = 'L123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru.'
# reg = r'[\w.-]+@[\w.]+[^. , ]{2,3}'
# print(re.findall(reg, s))


# text = '<body>пример жадного соответствия регулярного выражения</body>'
# print(re.findall('<.+?>', text))
# # *?, +?, ??
# # {m, n}?, {, n}?, {m,}?
#
# t = '2324 786 22 4569'
# reg = '\d{1,3}?'
# print(re.findall(reg, t))


# s = '<p>изображение <img alt="картинка" src="bg.jpg"> - фон страницы</p>'
# reg = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
# # reg = r'<img[^>]*>'
# print(re.findall(reg, s)) #<img src='bg.jpg'>



# s = "Python kjnkjnkjnkj [16] kmlkmlkmlkmlkm[17];lk;lk;lk;lk[18]."
# reg = r'\[[^]]+\]'
# print(re.findall(reg, s))


# s = "Петр и Ольга отлично учатся"
# reg = 'Петр|Виталий|Ольга'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# reg = r"(?:int|double)\s*=\s*\d+[.\w+]*" # () - сохраняющие и группирующие скобки; (?:) - группирующие не сохраняющие скобки
# print(re.findall(reg, s))


# s = '127.0.0.1'
# reg = r'(?:\d{1,3}.){1,3}(?:\d{1,3})'
# print(re.findall(reg, s))


# s = "Word2016, PS6, AI5"
# reg = r'([A-z]+)(\d*)'
# print(re.findall(reg, s))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 200000000000000 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])

print("hell")












































































































































