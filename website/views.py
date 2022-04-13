from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import *
from werkzeug.security import check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import os

views = Blueprint('views', __name__)
app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'website/static/images'


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/my_account', methods=['GET', 'POST'])
@login_required
def my_account():
    user = current_user.email
    my_recipes = get_user_recipes(user)
    if request.method == 'POST':
        if request.form['btn_identifier'] == 'add_recipe':
            recipe_name = request.form.get('recipe_name')
            ingredients = request.form.get('ingredients')
            instructions = request.form.get('instructions')
            servings = request.form.get('servings')
            reviews = request.form.get('review')
            difficulty = request.form.get('difficulty')
            uploaded_file = request.files['image_upload']
            uploaded_filename = uploaded_file.filename
            if uploaded_filename.lower().endswith((".jpg", '.jpeg', '.png')):
                if uploaded_filename != "":
                    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
            else:
                uploaded_filename = 'no_image_available.png'
                flash('No image has been uploaded.', category='error')

            if len(recipe_name) < 5:
                flash("Recipe name must be at least 5 characters.", category='error')
            elif len(ingredients) < 10:
                flash("Ingredients must be at least 10 characters.", category='error')
            elif len(instructions) < 20:
                flash("Ingredients must be at least 20 characters.", category='error')
            else:
                CSVRecipes(user, recipe_name, uploaded_filename, ingredients, instructions, servings, reviews, difficulty)
                write_to_file('recipes.csv')
                flash('Recipe has been added! See all your recipes on Recipes page.', category='success')
                my_recipes = get_user_recipes(user)

        if request.form['btn_identifier'] == "delete_recipe":
            recipe_name = request.form.get('delete_name')
            for rec in my_recipes:
                if rec.name == recipe_name:
                    all_recipes.remove(rec)
                    write_to_file('recipes.csv')
                    flash('Recipe has been removed!', category='success')
            my_recipes = get_user_recipes(user)

        if request.form['btn_identifier'] == "review_recipe":
            user_review = request.form.get('user_review')
            recipe_name = request.form.get('review_choice')
            for rec in my_recipes:
                if rec.name == recipe_name:
                    reviews = rec.reviews
                    if reviews != "":
                        reviews += ", " + user_review
                        rec.reviews = reviews
                    else:
                        rec.reviews = user_review
            flash('Review has been added!', category='success')
            write_to_file('recipes.csv')
            my_recipes = get_user_recipes(user)

    return render_template("my_account.html", all_recipes=my_recipes, user=current_user)


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.recipes'))
            else:
                flash("Incorrect password.", category='error')
        else:
            flash('Account does not exist.', category='error')

    return render_template("login.html", user=current_user)


@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.login'))


@views.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters!', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters!', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email, first_name, password1)
            starter_recipes(email)
            write_to_file("recipes.csv")
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully!', category='success')
            return redirect(url_for('views.recipes'))

    return render_template("sign_up.html", user=current_user)


@views.route('/recipes')
@login_required
def recipes():
    user = current_user.email
    my_recipes = get_user_recipes(user)
    return render_template("recipes.html", user=current_user, all_recipes=my_recipes)
