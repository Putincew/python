import json

class Stolice:
    def __init__(self):
        try:
            with open('Stolicy.json', 'r') as st:
                self.dic = json.load(st)
        except FileNotFoundError:
            self.dic = {}
            with open('Stolicy.json', 'w') as st:
                json.dump(self.dic, st)
        while True:
            if 'v' in locals():
                input('Нажмите ENTER, чтобы вернуться в меню')
            v = self.deistv()
            if v == 1:
                self.set_slov()
            elif v == 2:
                self.del_country()
            elif v == 3:
                self.poisk()
            elif v == 4:
                self.red_data()
            elif v == 5:
                self.show()
            elif v == 6:
                print('\nЗавершение работы')
                break
            else:
                print('\nВы ввели не существующую команду')
                
        
            
    def zapis(self):
        with open('Stolicy.json', 'w') as st:
            json.dump(self.dic, st)
        print('\nФайл сохранен')
    
    def deistv(self):
        a = '*'*30
        print(f'\n{a}\nВыбор дейстивя:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\n')
        n = int(input('Ввод: '))
        return n
        
    def set_slov(self):
        s = input('Введите название страны (с заглавной буквы): ')
        if s in self.dic:
            print("\nСтрана уже есть в базе\n")
        else:
            g = input('Введите название столицы (с заглавной буквы): ')
            self.dic[s] = g
            self.zapis()
            print(f'Страна {s} со столицей {g} добавлена в базу\n')
        
    def del_country(self):
        c = input('Введите название удаляемой страны (с заглавной буквы): ')
        if c in self.dic:
            del self.dic[c]
            self.zapis()
            print(f'\nСтрана {c} удалена\n')
        else:
            print('\nСтраны с таким назввнием нет в базе\n')
            
    def poisk(self):
        d = input('Введите название страны для поиска (с заглавной буквы): ')
        if d in self.dic:
            print(f'\nСтолица страны {d} - {self.dic[d]}\n')
        else:
            print('\nПоиск не нашел введенной страны\n')
            
    def red_data(self):
        a = input('Введите название страны для редактирования (с заглавной буквы): ')
        if a in self.dic:
            b = input('Введите новое название страны: ')
            c = input('Введите новое название столицы: ')
            del self.dic[a]
            self.dic[b] = c
            self.zapis()
            print(f'Страна {b} со столицей {c} теперь в базе')
        else:
            print('\nТакой страны нет в базе\n')
            
    def show(self):
        print()
        print(f'Страны в базе:\n{self.dic}')
        print()
        
    
        
Stolice()
        
    
            

        
    
            
