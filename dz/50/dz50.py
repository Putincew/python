from flask import Flask, render_template, url_for


app=Flask(__name__)
menu = [{"name":"Главная страница", "url": "index"},
        {"name":"О сайте", "url": "osite"},
        {"name":"Данные пользователя", "url": "form"}]


@app.route("/")
@app.route("/index")
def index():
    # print(url_for('index'))
    return render_template("index.html", title="Главная", menu=menu)

@app.route("/osite")
def osite():
    # print(url_for('about'))
    return render_template("osite.html", title="О сайте", menu=menu)



@app.route("/form", methods=["POST","GET"])
def form():
    return render_template("form.html", title="Оставьте свои данные", menu=menu)



@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"



if __name__=="__main__":
    app.run(debug=True)