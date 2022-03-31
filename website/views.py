from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", boolean=True)


@views.route('/recipes')
def recipes():
    return render_template("recipes.html")


@views.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")


@views.route('/login')
def login():
    return render_template("login.html")


@views.route('/account')
def account():
    return render_template("account.html")




