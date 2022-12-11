class Book:
    name_book = ''
    year = 0
    publisher = ''
    genre = ''
    autor = ''
    price = 0
    
    def set_name_book(self, name_book):
        self.name_book = name_book
        
    def get_name_book(self):
        print('Название книги:', self.name_book)


    def set_year(self, year):
        self.year = year
        
    def get_year(self):
        print('Год выпуска книги:', self.year, 'г.')


    def set_publisher(self, publisher):
        self.publisher = publisher
        
    def get_publisher(self):
        print('Издатель книги:', self.publisher)


    def set_genre(self, genre):
        self.genre = genre
        
    def get_genre(self):
        print('Жанр книги:', self.genre)


    def set_autor(self, autor):
        self.autor = autor
        
    def get_autor(self):
        print('Автор книги:', self.autor)


    def set_price(self, price):
        self.price = price
        
    def get_price(self):
        print('Стоимость книги:', self.price, 'р.')
        

       

b1 = Book()
b1.set_name_book("Изучаем Python")
b1.set_year(2009)
b1.set_publisher('Вильямс')
b1.set_genre('Компьютерная литература')
b1.set_autor('Марк Лутц')
b1.set_price(1000)

b1.get_name_book()
b1.get_year()
b1.get_publisher()
b1.get_genre()
b1.get_autor()
b1.get_price()
