from math import pi

class Table:
    def __init__(self, mes1=0, mes2=0):
        if mes2 == 0:
            self._radius = mes1
        else:
            self._width = mes1
            self._lenght = mes2

    def ploshad(self):
        raise NotImplementedError('метод должен быть во всех дочерних классах')


class Ktable(Table):
    def ploshad(self):
        return self._width * self._lenght


class Rtable(Table):
    def ploshad(self):
        return round(self._radius ** 2 * pi, 2)


k = Ktable(20, 10)
print(k.__dict__)
print(k.ploshad())
k1 = Ktable(20, 20)
print(k1.__dict__)
print(k1.ploshad())
r = Rtable(20)
print(r.__dict__)
print(r.ploshad())
