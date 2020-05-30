""" Рендеринг темплейтов, даже не знаю, что тут пояснять """
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # если запрос с формы, то собираем данные
    if not request.method == "POST":
        return render_template("contact.html")
    else:
        data = [request.form["username"], request.form["contact"], request.form["message"]]
        # здесь типо отправляем данные в бд
        return render_template("contact.html", message=True)


@app.route("/about")
def about():
    return render_template("about.html")
    