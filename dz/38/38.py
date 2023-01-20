class Descriptor:
    @staticmethod
    def verify(lenth):
        if not isinstance(lenth, int) or lenth <= 0:
            raise TipeError('Должно быть задано целое положительное число.')
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
        
    def __set__(self, instance, value):
        self.verify(value)
        instance.__dict__[self.name] = value
        
        
class Triangle:
    a = Descriptor()
    b = Descriptor()
    c = Descriptor()
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    @staticmethod
    def verif_trian(a, b, c):
        if a+b<c or a+c<b or c+b<a:
            return True
        else:
            return False
        
    def __str__(self):
        if self.verif_trian(self.a, self.b, self.c):
            return f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует.'
        else:
            return f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует.'
            
            
t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)
print(t1)
print(t2)
print(t3)