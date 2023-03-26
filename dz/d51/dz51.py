from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
import os
import sqlite3
from FDateBase import FDateBase

DATABASE="/tmp/d51.db"
DEBUG = True
SECRET_KEY = '12345678910'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path,'d51.db'))

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
    return render_template("index.html", title="Главная", menu=dbase.get_menu())

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

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'link_db'):
        g.link_db.close()

if __name__=="__main__":
    app.run(debug=True)