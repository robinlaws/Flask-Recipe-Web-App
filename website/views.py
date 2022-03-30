from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", boolean=True)


@views.route('/recipes')
def recipes():
    return render_template("recipes.html")




