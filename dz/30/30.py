class Ploshad:
    count = 0
    
    @staticmethod
    def tree_geron(a, b, c):
        Ploshad.count += 1
        p = 0.5 * (a + b + c)
        return f'Площадь треугольника по формуле Герона ({a}, {b}, {c}): {(p * (p - a) * (p - b) * (p - c)) ** 0.5}'

    @staticmethod
    def tree_hos(osn, h):
        Ploshad.count += 1
        return f'Площадь треугольника через основание и высоту ({osn}, {h}): {round(osn * h / 2, 2)}'

    @staticmethod
    def qwadr(x):
        Ploshad.count += 1
        return f'Площадь квадрата ({x}): {x**2}'

    @staticmethod
    def pryamoug(z, y):
        Ploshad.count += 1
        return f'Площадь прямоугольника ({z}, {y}): {z * y}'

    @staticmethod
    def counter():
        return f'Количество подсчетов площади: {Ploshad.count}'


cl = Ploshad()
print(cl.tree_geron(3, 4, 5))
print(cl.tree_hos(6, 7))
print(cl.qwadr(7))
print(cl.pryamoug(2, 6))
print(cl.counter())