import random

class Cat:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        if self.sex != 'M' and self.sex != 'F':
            raise TypeError('допустимые значения пола "M" или "F"')

    def __add__(self, other):
        if self.sex == other.sex:
            return 'Пол должен быть разным'

        print(f'{self.name} is good boy!!!' if self.sex == 'M' else f'{self.name} is good girl!!!')
        print(f'{other.name} is good boy!!!' if other.sex == 'M' else f'{other.name} is good girl!!!')
        return [f'Cat{i} (name="No name", age=0, sex={random.choice(["M", "F"])})' for i in range(1, random.randint(2, 8))]

c1 = Cat('Tom', 'M')
c2 = Cat('Elsa', 'F')
print(c1 + c2)