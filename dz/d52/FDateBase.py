import sqlite3

class FDateBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql="SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_post(self, title, text, price):
        try:
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, price))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления курса в БД" + str(e))
            return False
        return True

    def get_post(self, post_id):
        try:
            self.__cur.execute(f"SELECT title, text, price FROM posts WHERE id = {post_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД" + str(e))

        return False, False

    def get_posts_announce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text, price FROM posts")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД" + str(e))

        return []