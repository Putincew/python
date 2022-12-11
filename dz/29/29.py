class Rectangle:
    
    def __init__(self, len_x, len_y):
        self.__len_x = len_x
        self.__len_y = len_y

    def set_xy(self, x, y):
        self.__len_x = x
        self.__len_y = y
        

    def get_xy(self):
        print('Ширина прямоугольника:', self.__len_x)
        print('Высота прямоугольника:', self.__len_y)

    def rect_square(self):
        print('Площадь прямоугольника:', self.__len_x * self.__len_y)
        
    def rect_perimetr(self):
        print('Периметр прямоугольника:', (self.__len_x + self.__len_y) * 2)
        
    def rect_diagonal(self):
        print('Диагональ прямоугольника:', round((self.__len_x**2 + self.__len_y**2)**0.5, 2))
        
    def rect_paint(self):
        print(('*' * self.__len_x + '\n') * self.__len_y)
        
        
r1 = Rectangle(0, 0)
r1.set_xy(9, 3)
r1.get_xy()
r1.rect_square()
r1.rect_perimetr()
r1.rect_diagonal()
r1.rect_paint()
