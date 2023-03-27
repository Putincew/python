from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
import os
import sqlite3
from FDateBase import FDateBase

DATABASE="/tmp/d52.db"
DEBUG = True
SECRET_KEY = '12345678910'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path,'d52.db'))

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
    if not hasattr(g,'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("index.html", title="Главная", menu=dbase.get_menu(), posts=dbase.get_posts_announce())

@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDateBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['price'])
            if not res:
                flash("Ошибка добавления курса", category='error')
            else:
                flash("Курс добавлен успешно", category='success')
        else:
            flash("Ошибка добавления курса", category='error')

    return render_template("add_post.html", title="Добавление курса", menu=dbase.get_menu())


@app.route("/post/<int:id_post>")
def show_post(id_post):
    db = get_db()
    dbase = FDateBase(db)
    title, post, price = dbase.get_post(id_post)
    if not title:
        abort(404)

    return render_template('post.html', title=title, post=post, price=price, menu=dbase.get_menu())

@app.route("/osite")
def osite():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("osite.html", title="О сайте", menu=dbase.get_menu())



@app.route("/form", methods=["POST","GET"])
def form():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("form.html", title="Оставьте свои данные", menu=dbase.get_menu())



@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__=="__main__":
    app.run(debug=True)