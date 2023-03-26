import sqlite3
import os
from flask import Flask, render_template, url_for, flash, session, redirect, abort
from FDateBase import FDateBase


# конфигурация
DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'kjnkj4jkn6kjkj3nkjk56jnk4kj23'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'flsk.db'))

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

menu = [{'name': 'главная', 'url': 'index'},
        {"name": "онас", "url": 'about'},
        {"name": "обратная связб", "url": "content"}]

@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("index.html", title='главная', menu=dbase.get_menu(), post=dbase.get_post_announce())



@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    db = get_db()
    dbase = FDateBase(db)

    return render_template('add_post.html', title='добавление статьи', menu=dbase.get_menu())


@app.route('/post/<int:id_post>')
def show_post(id_post):
    db = get_db()
    dbase = FDateBase(db)
    title, post = dbase.get_post(id_post)
    if not title:
        abort(404)

    return render_template('post.html', title=title, post=post, menu=dbase.get_menu())


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    if len(request.form['username']) > 2:
        flash('сообщ отправлено', category='success')
    else:
        flash('ошибка отправления', category='error')

    print(request.form)

    return render_template("contact.html", title)

@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'пользователь {username}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return redirect('login.html', title='авторизация')


@app.errorhandler(404)
def page_not_found():
    return render_template('page404.html', title='страница не найдена', menu=menu)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == '__main__':
    app.run(debug=True)