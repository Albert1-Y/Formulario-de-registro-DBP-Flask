from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=["POST"])
def login():
	name = request.form.get("name")
	return render_template("session.html",name=name,)

@app.route("/abc")
def clipi():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    surname = request.form.get("surname")
    correo = request.form.get("correo")
    passw = request.form.get("passw")
    birthday_day  = request.form.get("birthday_day")
    birthday_month = request.form.get("birthday_month")
    birthday_year = request.form.get("birthday_year")

    return render_template("ver_register.html",name = name, surname = surname, correo = correo, passw = passw, birthday_day = birthday_day, birthday_month = birthday_month, birthday_year = birthday_year)


@app.route("/<string:name>")
def session(name):
	return render_template("session.html", name=name)


@app.route("/users")
def names():
    # qconsultar una base de datos.
    names_list = ["Jose", "Pedro", "Maria"]
    return render_template("list.html", names = names_list)



