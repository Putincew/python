

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




import sqlite3 as sq

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



# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     ALTER TABLE person_table
#     RENAME COLUMN address TO home_address
#     ''')







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

# with sq.connect('db_3.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     SELECT *
#     FROM T1
#     ORDER BY FName
#     LIMIT 2, 5
#     ''')
#
#     res = cur.fetchone()
#     res2 = cur.fetchmany()
#     # res = cur.fetchall()
#     print(res)
#     print(res2)
#     # for res in cur:
#     #     print(res)

# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     ''')
#con.commit()
#con.close() если без with


# cars = [
#     ("Renault", 20000),
#     ("volvo", 29000),
#     ("mers", 57000),
#     ("ben", 35000),
#     ("audy", 52000),
# ]
# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS cars(
#          car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#          model TEXT,
#          price INTEGER)''')
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # for car in cars:
    #     cur.execute('INSERT INTO cars VALUES(NULL, ?, ?)', car)

    # cur.executemany('INSERT INTO cars VALUES(NULL, ?, ?)', cars)

    # cur.execute('INSERT INTO cars VALUES(1, "Renault", 20000)')
    # cur.execute('INSERT INTO cars VALUES(2, "volvo", 29000)')
    # cur.execute('INSERT INTO cars VALUES(3, "mers", 57000)')
    # cur.execute('INSERT INTO cars VALUES(4, "ben", 35000)')
    # cur.execute('INSERT INTO cars VALUES(5, "audy", 52000)')




# con = None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#           car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#           model TEXT,
#           price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, "Renault", 20000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print(f'Ошибка выполнения {e}')
# finally:
#     if con:
#         con.close()



# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS cars(
#          car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#          model TEXT,
#          price INTEGER)''')
#
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     rows = cur.fetchmany(5)
#     # print(rows)
#     for res in cur:
#         print(res['model'], res['price'])


# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IDError as e:
#         print(e)
#         return False
#
#
# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS users(
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ava BLOB
#     );
#     ''')
#
#     img = read_ava(1)
#     if img:
#         binary = sq.Binary(img)
#         cur.execute("INSERT INTO users VALUES (?, ?)", (1, binary))


with sq.connect('cars.db') as con:
    cur = con.cursor()
    # with open("sql_dump.sql", "w") as f:
    #     for sql in con.iterdump():
    #         f.write(sql)
    with open("sql_dump.sql", "r") as f:
        sql = f.read()
        cur.executescript(sql)



















