class Auto:
    def __init__(self, model, year, manufactur, power, color, price):
        self.verify_str(model)
        self.verify_year(year)
        self.verify_str(manufactur)
        self.verify_str(power)
        self.verify_str(color)
        self.verify_price(price)

        self.__model = model
        self.__year = year
        self.__manufactur = manufactur
        self.__power = power
        self.__color = color
        self.__price = price

    @staticmethod
    def verify_str(text):
        if not isinstance(text, str):
            raise TypeError('Не верный формат. Должна быть строка')

    @staticmethod
    def verify_price(num):
        if not isinstance(num, int):
            raise TypeError('не верный формат. Должно быть число')

    @staticmethod
    def verify_year(year):
        if not year.isdigit() or len(year) != 4:
            raise TypeError('В строке должно быть 4 цифры')

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.verify_str(new_model)
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.verify_year(new_year)
        self.__year = new_year

    @property
    def manufactur(self):
        return self.__manufactur

    @manufactur.setter
    def manufactur(self, new_manufactur):
        self.verify_str(new_manufactur)
        self.__manufactur = new_manufactur

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, new_power):
        self.verify_str(new_power)
        self.__power = new_power

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.verify_str(new_color)
        self.__color = new_color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.verify_price(new_price)
        self.__price = new_price

    def auto_info(self):
        print('*' * 10, 'Данные автомобиля', '*' * 10)
        print('Название модели:', self.__model)
        print('Год выпуска:', self.__year)
        print('Производитель:', self.__manufactur)
        print('Мощность двигателя:', self.__power)
        print('Цвет машины:', self.__color)
        print('Цена:', self.__price)


bmw = Auto('BMW', '2021', 'BMW', '538 л.с.', 'White', 10790000)

bmw.auto_info()
