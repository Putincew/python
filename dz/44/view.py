def add_title(text):
    def wraper(fn):
        def wrap(self, *arg):
            print(text.center(50, '='))
            res = fn(self, *arg)
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
