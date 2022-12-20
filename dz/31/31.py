# вариант1
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_us = 'USD'
    suffix_eur = 'EUR'
    def __init__(self, num, syrname, percent, value=0):
        self.__num = num
        self.__syrname = syrname
        self.__percent = percent
        self.__value = value
        print(f'счет № {self.__num} принадлежащий {self.__syrname} был открыт')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'счет № {self.__num} принадлежащий {self.__syrname} был закрыт.')

    def get_num(self):
        print(self.__num)

    def set_num(self, new_num):
        self.__num = new_num

    def get_surname(self):
        print(self.__syrname)

    def set_surname(self, new_surname):
        self.__syrname = new_surname

    def get_percent(self):
        print(self.__percent)

    def set_percent(self, new_percent):
        self.__percent = new_percent

    def get_value(self):
        print(self.__value)

    def set_value(self, new_value):
        self.__value = new_value

    def print_balance(self):
        print(f'текущий баланс {self.__value} {Account.suffix}')

    def print_info(self):
        print('информация о счете')
        print('-'*20)
        print(f'# {self.__num}')
        print(f'владелец: {self.__syrname}')
        self.print_balance()
        print(f'проценты: {self.__percent:.0%}')
        print('-'*20)

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname):
        self.__syrname = surname

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'состояние счета: {usd_val} {Account.suffix_us}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'состояние счета: {eur_val} {Account.suffix_eur}')

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('проценты были начислены')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'у вас нет такой суммы {val} {Account.suffix}')
            self.print_balance()
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято')
            self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно зачислено')
        self.print_balance()


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()

Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.edit_owner('Дюма')
acc.print_info()
acc.add_percents()
acc.withdraw_money(3000)
print()
acc.withdraw_money(100)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)
print()

acc.set_num('55555')
acc.set_surname('Новый')
acc.set_percent(100)
acc.set_value(500)
acc.get_num()
acc.get_surname()
acc.get_percent()
acc.get_value()









# вариант2
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_us = 'USD'
    suffix_eur = 'EUR'
    def __init__(self, num, syrname, percent, value=0):
        self.__num = num
        self.__syrname = syrname
        self.__percent = percent
        self.__value = value
        print(f'счет № {self.__num} принадлежащий {self.__syrname} был открыт')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'счет № {self.__num} принадлежащий {self.__syrname} был закрыт.')

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, new_num):
        self.__num = new_num

    @property
    def surname(self):
        return self.__syrname

    @surname.setter
    def surname(self, new_surname):
        self.__syrname = new_surname

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, new_percent):
        self.__percent = new_percent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def print_balance(self):
        print(f'текущий баланс {self.__value} {Account.suffix}')

    def print_info(self):
        print('информация о счете')
        print('-'*20)
        print(f'# {self.__num}')
        print(f'владелец: {self.__syrname}')
        self.print_balance()
        print(f'проценты: {self.__percent:.0%}')
        print('-'*20)

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname):
        self.__syrname = surname

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'состояние счета: {usd_val} {Account.suffix_us}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'состояние счета: {eur_val} {Account.suffix_eur}')

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('проценты были начислены')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'у вас нет такой суммы {val} {Account.suffix}')
            self.print_balance()
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято')
            self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно зачислено')
        self.print_balance()


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()

Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.edit_owner('Дюма')
acc.print_info()
acc.add_percents()
acc.withdraw_money(3000)
print()
acc.withdraw_money(100)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)
print()

acc.num = '55555'
acc.surname = 'Новый'
acc.percent = 100
acc.value = 500
print(acc.num)
print(acc.surname)
print(acc.percent)
print(acc.value)


