def add_title(text):
    def wraper(fn):
        def wrap(*args, **kwargs):
            print(text.center(50, '='))
            res = fn(*args, **kwargs)
            print('=' * 50)
            return res
        return wrap
    return wraper

class UserInterface:

    @add_title(' Ввод пользовательских данных ')
    def wait_user_answer(self):
        print('Действия с фильмами:')
        print('1 - добавление фильма'
              '\n2 - каталог фильмов'
              '\n3 - просмотр определенного фильма'
              '\n4 - удаление фильма')
        print('q - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    @add_title('  добавление фильма ')
    def add_user_film(self):
        dict_film = {
            'название': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'продолжительность': None,
            'студия': None,
            'актеры': None
        }
        for key in dict_film:
            dict_film[key] = input(f'введите {key} фильма: ')

        return dict_film

    @add_title('каталог фильмов: ')
    def show_all_films(self, films):

        for ind, film in  enumerate(films, 1):
            print(f'{ind}. {film}')

    @add_title('ввод названия фильма: ')
    def get_user_film(self):
        user_film = input('введите название фильма: ')
        return user_film

    @add_title('просмотр фильма: ')
    def show_single_film(sejf, film):
        for key in film:
            print(f'{key} фильма - {film[key]}')

    @add_title('сообщение об ошибке')
    def show_incorrect_title_error(self, user_title):
        print(f'фильм {user_title} не существует')

    @add_title('удаление фильма')
    def remove_single_film(self,film):
        print(f'фильм {film} был удален')

    @add_title('сообщение об ошибке')
    def show_incorrect_answer_error(self, answer):
        print(f'варианта {answer} не существует')

