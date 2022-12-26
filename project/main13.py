# ООП

# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1 # свойства(поля, переменные)
#
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))
#
# p1 = Point() # создали экземпляр класса
# p2 = Point() # создали экземпляр класса
# print(p1.x)
# print(Point.x)
# p1.x = 100
# p2.x = 200
# print(p1.x)
# print(p2.x)
# print(Point.x)
# print(id(p1))
# print(id(p2))
# print(id(Point))
# Point.y = 300
# print(p1.y)
# print(p2.y)
# print(Point.y)

#
# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y)
# print(p1.__dict__)
# # print(Point.__dict__)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self):# self принимает экземпляр класса
#         # print('метод set_coord')# метод(функция) класса. Атрибуты - свойства + методы
#         print(self.__dict__)
#
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# Point.set_coord(p1)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)


# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     adress = 'street, house'
#
#     def print_info(self):
#         print('Персональные данные '.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nАдресс: {self.adress}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, adress):
#         self.name = first_name
#         self.birthday = birthday
#         self.country = country
#         self.phone = phone
#         self.city = city
#         self.adress = adress
#
#     def set_name(self, name):
#         if isinstance(name, str):
#             self.name = name
#
#     def get_name(self):
#         return self.name
#
# h1 = Human()
# h1.print_info()
# h1.input_info('юля', '23.05.1985', '44-56-85', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_name("Алефтина")
# print(h1.get_name())


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
#     def print_info(self):
#         print('Данные сотрудника: ', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника: ', self.skill, '\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
#
# p1 = Person('Anna', 'Dolgih')
# p1.print_info()
# p1.add_skill(2)


# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print('Конструктор')
#     #     return  super().__new__(cls)
#
#
#     def __init__(self, x, y):
#         print('инициализатор')
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print('Удаление экземпляра', self.__class__.__name__)
#
#     def print_coord(self):
#         print(f'x: {self.x}, y: {self.y}')
#
#
#
# p1 = Point(5, 10)
# # print(p1.__dict__)
# p1.print_coord()
# print(id(p1))
#
# p2 = Point(2, 7)
# # del p2
# p2.print_coord()
# print(id(p2))


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
# p1 = Point(5, 10)
# # print(p1.count)
# p2 = Point(7, 2)
# # print(p2.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота:', self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается')
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#         else:
#             print('Работающих роботов осталось', Robot.k)
#
#     def say_hi(self):
#         print('Приветствую. Меня зовут', self.name)
#
#
#
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('Численность роботов: ', Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Численность роботов: ', Robot.k)
#
# print('\nЗдесь роботы делают работу\n')
# print('Роботы сделали свою работу. Давайте их выключим.')
# del droid1
# del droid2
# print('Численность роботов: ', Robot.k)


# class Point:
#     __slots__ = ['__x', '__y', 'z']
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('координаты должны быть цифрами')
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# #
# p1 = Point(5, 10)
# p1.z = 15
# print(p1.z)
# # print(p1.__dict__)
# # print(p1.get_coord())
# # p1.set_coord(1, 2)
# # print(p1.get_coord())
# # print(p1.x, p1.y)
# # p1.x = 100
# # p1.y = 'abc'
# # print(p1.x, p1.y)
# # print(p1.__dict__)
# p1._Point__x = 111
# # print(p1.__dict__)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print('вызов __set_x')
#         self.__x = x
#
#     def __get_x(self):
#         print('вызов __get_x')
#         return self.__x
#
#     def __del_x(self):
#         print('удаление свойства')
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         print('вызов __get_x')
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print('вызов __set_x')
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print('удаление свойства')
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('килограммы задаются только числами')
#
#     def to_poundas(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, 'кг =>', end=' ')
# print(weight.to_poundas(), 'фунтов')
# weight.kg = 2.3
# print(weight.kg, 'кг =>', end=' ')
# print(weight.to_poundas(), 'фунтов')


# class Person():
#     def __init__(self, name, skill):
#         self.__name = name
#         self.__skill = skill
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         print('удаление свойства')
#         del self.__name
#
#     @property
#     def skill(self):
#         return self.__skill
#
#     @skill.setter
#     def skill(self, new_skill):
#         self.__skill = new_skill
#
#     @name.deleter
#     def skill(self):
#         print('удаление свойства')
#         del self.__skill
#
#
# p1 = Person('Viktor', 12)
# # print(p1.name)
# print(p1.skill)


#
# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(4, 8)
# p3 = Point(2, 7)
# print(p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x - 1
#
#     @staticmethod
#     def dec(x):
#         return x + 1
#
# c1 = Change()
# print(Change.inc(10), Change.dec(10))
# print(c1.inc(10), c1.dec(10))



# class Args:
#     @staticmethod
#     def max(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def min(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def arif(a, b, c, d):
#         return sum((a,b,c,d))
#
#     @staticmethod
#     def factor(x):
#         first = 1
#         for i in range(1, x+1):
#             first *= i
#         return first
#
#
#
# print(Args.max(3, 5, 7, 9))
# print(Args.min(3, 5, 7, 9))
# print(Args.arif(3, 5, 7, 9))
# print(Args.factor(6))


# class Data:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#
#     def string_to(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# string_date = Data.from_string('23.10.2022')
# print(string_date.string_to())

#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_us = 'USD'
#     suffix_eur = 'EUR'
#     def __init__(self, num, syrname, precent, value=0):
#         self.num = num
#         self.syrname = syrname
#         self.precent = precent
#         self.value = value
#         print(f'счет № {self.num} принадлежащий {self.syrname} был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'счет № {self.num} принадлежащий {self.syrname} был закрыт.')
#
#
#     def print_balance(self):
#         print(f'текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print('информация о счете')
#         print('-'*20)
#         print(f'# {self.num}')
#         print(f'владелец: {self.syrname}')
#         self.print_balance()
#         print(f'проценты: {self.precent:.0%}')
#         print('-'*20)
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.syrname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'состояние счета: {usd_val} {Account.suffix_us}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def add_percents(self):
#         self.value += self.value * self.precent
#         print('проценты были начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'у вас нет такой суммы {val} {Account.suffix}')
#             self.print_balance()
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято')
#             self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно зачислено')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# acc.add_percents()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)



# import re
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_ps(ps)
#         self.__fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('не верный формат фио')
#         letters = ''.join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефис')
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('возраст должен быть числом от 14 до 120')
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError('вес должен быть вещественным числом от 20кг и выше')
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError('паспорт должен быть строкой')
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('не верный формат паспорта')
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError('серия и номер паспорта должны быть цифрами')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
#
#
# p1 = UserData('Волков Игорь Николаевич', 26, '1234 567890', 80.8)
# p1.fio = 'Сидоров Игорь Николаевич'



# наследование


# class Point(object):
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}), ({self.__y})'
#
# # print(issubclass(Point, object))
# # print(dir(Point))
#
#
# class Prop:
#     def __init__(self, sp:Point, ep:Point, color:str='red', width:int=1):
#         print('инициализатор базового класса')
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
# class Line(Prop):
#     def __init__(self, *args):
#         print('переопределенный инициализатор line')
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self) -> str:
#         return f'рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}'
#
#
# class Rect(Prop):
#     def draw_rect(self) -> str:
#         print(f'рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# print(line.draw_line())
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
#
# # DRY (Don't Repeat you self) - не повторяйся


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def __str__(self):
#         return self.__color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     def __str__(self):
#         return f'{self.__width}, {self.__height}, {self.color}'
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('ширина должна быть положительной')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError('высота должна быть положительной')
#
#     def area(self):
#         return self.__width * self.__height
#
# rect = Rectangle(10, 20, 'green')
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = 'red'
# print(rect)
# rect.width = 5
# print(rect)
# print(rect.area())



# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print('фон:', self.fon)


# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.border = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print('рамка:', self.border)


# class RectFonBorder(RectFon):
#     def __init__(self, width, height, background, border):
#         super().__init__(width, height, background)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print('рамка:', self.border)


# shape = Rect(100, 200)
# shape.show_rect()
#
# shape1 = RectFon(400, 300, 'yellow')
# shape1.show_rect()
# print()
# # shape2 = RectBorder(600, 500, '1px solid red')
# # shape2.show_rect()
#
# shape3 = RectFonBorder(600, 500, 'yellow', '1px solid red')
# shape3.show_rect()


# class Vector(list):
#     def __str__(self):
#         return ''.join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))





# перегрузка методов


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print('координты должны быть целым числом')
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep = None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(50, 60))
# line.draw_line()
# line.set_coord(Point(200, 400))
# line.draw_line()




# абстрактные методы


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_int(self):
        if not isinstance(self.__x, int) or not isinstance(self.__y, int):
            print("Координаты должны быть целочисленными")
            return False
        return True


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def draw_line(self):
        raise NotImplementedError('в дочернем классе должен быть определен метод draw')


class Line(Prop):
    # def draw_line(self):
    #     print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
    pass


line = Line(Point(1, 2), Point(10, 20))
line.draw_line()


















