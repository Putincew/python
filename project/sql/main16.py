

#
# from parsers import Parsers
#
#
# def main():
#     pars = Parsers('https://www.ixbt.com/live/index/news/', 'new.txt')
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()




import sqlite3

# con = sqlite3.connect('profile.db')
# cur = con.cursor()
#
# cur.execute('''
# ''')
#
# con.close()

# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     # cur.execute('''CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa BLOB
#     # )''')
#     cur.execute('DROP TABLE users')



with sqlite3.connect('users.db') as con:
    cur = con.cursor()
    cur.execute('''
    ALTER TABLE person_table
    RENAME COLUMN address TO home_address
    ''')







# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS person_table(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB DEFAULT '+798900000000',
#     age INTEGER NOT NULL CHECK(age>15 AND age<70),
#     email TEXT UNIQUE
#     )''')
#     cur.execute('DROP TABLE person_table')
















































