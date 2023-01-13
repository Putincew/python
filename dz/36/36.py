class Shape:
    def __init__(self, color):
        self.color = color
        if not isinstance(self.color, str):
            raise TypeError('Прамаметр цвет должен быть строкой')
        
    def perimetr(self):
        raise NotImplemented('Во всех дочерних классах должен быть метод perimetr')
        
    def area(self):
        raise NotImplemented('Во всех дочерних классах должен быть метод area')
        
    def paint_shape(self):
        raise NotImplemented('Во всех дочерних классах должен быть метод paint_shape')
        
    def info(self):
        raise NotImplemented('Во всех дочерних классах должен быть метод info')
        

class Square(Shape):
    def __init__(self, stor, color):
        self.stor = stor
        super().__init__(color)
        if not isinstance(self.stor, int):
            raise TypeError('Сторона квадрата должна быть целым числом')
        
    def perimetr(self):
        return self.stor * 4
        
    def area(self):
        return self.stor **2
        
    def paint_shape(self):
        return ('*' * self.stor + '\n') * self.stor
        
    def info(self):
        print('===Квадрат===')
        print('Сторона:', self.stor)
        print('Цвет:', self.color)
        print('Площадь:', self.area())
        print('Периметр:', self.perimetr())
        print(self.paint_shape())
    
    
    
class Rectangle(Shape):
    def __init__(self, weight, height, color):
        self.weight = weight
        self.height = height
        super().__init__(color)
        if not isinstance(self.weight, int) or not isinstance(self.height, int):
            raise TypeError('Сторона прямоугольника должна быть целым числом')
        
    def perimetr(self):
        return self.weight * 2 + self.height * 2
        
    def area(self):
        return self.weight * self.height
        
    def paint_shape(self):
        return ('*' * self.weight + '\n') * self.height
        
    def info(self):
        print('===Прямоугольник===')
        print('Высота:', self.height)
        print('Ширина:', self.weight)
        print('Цвет:', self.color)
        print('Площадь:', self.area())
        print('Периметр:', self.perimetr())
        print(self.paint_shape())
    
    
    
class Triangle(Shape):
    def __init__(self, st1, st2, st3, color):
        self.st1 = st1
        self.st2 = st2
        self.st3 = st3
        super().__init__(color)
        if not isinstance(self.st1, int) or not isinstance(self.st2, int) or not isinstance(self.st3, int):
            raise TypeError('Сторона треугольника должна быть целым числом')
        
    def perimetr(self):
        return self.st1 + self.st2 + self.st3
        
    def area(self):
        p = (self.st1 + self.st2 + self.st3)/2
        return round((p*(p-self.st1)*(p-self.st2)*(p-self.st3))**0.5, 2)
        
    def paint_shape(self):
        probel = self.st2 - 1
        count = 1
        stroka = ''
        while count <= self.st1:
            stroka += ' ' * probel + '*' * count + '\n'
            probel -= 1
            count += 2
            
        return stroka
        
    def info(self):
        print('===Треугольник===')
        print('Сторона1:', self.st1)
        print('Сторона2:', self.st2)
        print('Сторона3:', self.st3)
        print('Цвет:', self.color)
        print('Площадь:', self.area())
        print('Периметр:', self.perimetr())
        print(self.paint_shape())
        
        
s = Square(3, 'red')
r = Rectangle(7, 3, 'green')
t = Triangle(11, 6, 6, 'yellow')

s.info()
r.info()
t.info()