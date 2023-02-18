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
        print('Действия со статьями:')
        print('1 - создание статьи'
              '\n2 - просмотр статей'
              '\n3 - просмотр определенной статьи'
              '\n4 - удаление статьи')
        print('q - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    @add_title('  создание статьи ')
    def add_user_article(self):
        dict_article = {
            'название': None,
            'автор': None,
            'количество страниц': None,
            'описание': None
        }
        for key in dict_article:
            dict_article[key] = input(f'введите {key} статьи: ')

        return dict_article

    @add_title('список статей: ')
    def show_all_articles(self, articles):

        for ind, article in  enumerate(articles, 1):
            print(f'{ind}. {article}')

    @add_title('ввод названия статьи: ')
    def get_user_article(self):
        user_article = input('введите название статьи')
        return user_article

    @add_title('просмотр статьи: ')
    def show_single_article(sejf, article):
        for key in article:
            print(f'{key} статья - {article[key]}')

    @add_title('сообщение об ошибке')
    def show_incorrect_title_error(self, user_title):
        print(f'статья {user_title} не существует')

    @add_title('удаление статьи')
    def remove_single_article(self,article):
        print(f'статья {article} была удалена')

    @add_title('сообщение об ошибке')
    def show_incorrect_answer_error(self, answer):
        print(f'варианта {answer} не существует')
