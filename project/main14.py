# from  car import electrocar
#
# def run():
#
#     e_car = electrocar.ElectroCar('Tesla', 'T', 2020, 50000)
#     e_car.show_car()
#     e_car.description_battery()
#
# if __name__ == '__main__':
#     run()


# Упаковка данных
# кодирование(сериализация)
# декодирование(десериализация)

# 1.marshal (.pyc)
# 2.pickle
# 3.json

# dump() - сохраняет данные в файл
# load() - чтение данных из открытого файла
#
# dumps() - сохраняем данные в строку (в памяти)
# loads() - считывает данные из строки (из памяти)


# import pickle
#
# filename = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': ['морковь'],
#     'бюджет': 1000
# }
#
# with open(filename, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, 'rb') as fh:
#     shop = pickle.load(fh)
#
# print(shop)


# import pickle

# class Test:
#     num = 35
#     st = 'Привет'
#     lst = [1,2,3]
#     d = {'first': 'a', 'second': 2}
#     tpl = (22,33)
#
#     def __str__(self):
#         return f'число: {Test.num}\nстрока: {Test.st}\nсписок: {Test.lst}\nсловарь: {Test.d}\nкортеж: {Test.tpl}'
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(f'сериализация в строку: \n{my_obj}\n')
#
# l_obj = pickle.loads(my_obj)
# print(f'Десериализация в строку: \n{l_obj}\n')

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x*x
#
#     def __str__(self):
#         return f'{self.a}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)


#
# import json
#
# data = {
#     'name': 'Igor',
#     'hobbies': ('running', 'sky diving'),
#     'age': 20,
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 5
#         },
# {
#             'firstName': 'Bob',
#             'age': 8
#         }
#     ]
# }
#
# # with open("data_file.json", "w") as fw:
# #     json.dump(data, fw, indent=4)
# #
# # with open("data_file.json", "r") as fw:
# #     data = json.load(fw)
# #     print(data)
#
# json_string = json.dumps(data)
# data = json.loads(json_string)
# print(data)


# import json
# from random import choice
#
#
# def get_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
# persons = []
# for i in range(5):
#     write_json(get_person())
import json

class Student:
    def __init__(self, name, ranks):
        self.name = name
        self.ranks = ranks

    def __str__(self):
        # a = ''
        # for i in self.ranks:
        #     a += f'{i}, '
        a = ', '.join(map(str, self.ranks))

        return  f'студент: {self.name} {a}'

    def add_ranks(self, rank):
        self.ranks.append(rank)

    def delete_rank(self, index):
        self.ranks.pop(index)

    def edit_rank(self, index, new_rank):
        self.ranks[index] = new_rank

    def average_rank(self):
        return round(sum(self.ranks) / len(self.ranks), 2)

    @staticmethod
    def dump_to_json(stud, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = []

        data.append({'name': stud.name, 'marks': stud.ranks})
        with open(filename, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load_to_file(filename):
        with open(filename, 'r') as f:
            print(json.load(f))



class Group:
    def __init__(self, studente, group):
        self.studente = studente
        self.group=group

    def __str__(self):
        a = ''
        for i in self.studente:
            a += str(i) + '\n'
        return f'группа: {self.group}\n{a}\n'

    def add_student(self, student):
        self.studente.append(student)

    def remove_student(self, index):
        return self.studente.pop(index)

    @staticmethod
    def change_group(group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    @staticmethod
    def dump_group(file, group):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = []

        with open(file, 'w')as f:
            stud_list = []
            for i in group.studente:
                stud_list.append([i.name, i.ranks])
            data.append(stud_list)
            json.dump(data, f, indent=2)

    @staticmethod
    def upload_journal(file):
        with open(file, 'r') as f:
            print(json.load(f))




# st1 = Student('bon', [5,4,3,4,3,5])
# print(st1)
# st1.add_ranks(4)
# print(st1)
# st1.delete_rank(3)
# print(st1)
# st1.edit_rank(2, 4)
# print(st1)
# print(st1.average_rank())


st1 = Student('bon', [5,4,3,4,3,5])


st2 = Student('nik', [2,5,4,5,1,3])
#
st3 = Student('bir', [1,3,5,5,1,2])
sts = [st1, st2]
my_group = Group(sts, 'гк питон')
# print(my_group)
my_group.add_student(st3)
# print(my_group)
# print()
my_group.remove_student(1)
# print(my_group)
# print(my_group)
group22 = [st2]
my_group2 = Group(group22, 'гк веб')
Group.dump_group('group.json', my_group)
Group.upload_journal('group.json')
# print(my_group2)

Student.dump_to_json(st1, 'student.json')
Student.load_to_file('student.json')
print(st1)

Student.dump_to_json(st2, 'student.json')
Student.load_to_file('student.json')
print(st2)










