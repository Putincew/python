import json


class Test2:
    def __init__(self):
        self.a = 35
        self.b = 'test'
        self.c = lambda x: x*x

    def __str__(self):
        return f'{self.a}, {self.b}, {self.c}'


item1 = Test2()
item2 = json.dumps(item1.__str__())
item3 = json.loads(item2)
print('Запись в память:', item3)

with open('test2.json', 'w') as fw:
    json.dump(Test2().__str__(), fw)

with open('test2.json', 'r') as fw:
    data = json.load(fw)
    print('Запись в файл:', data)