from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Recipe
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .static import recipe_dict as r

auth = Blueprint('auth', __name__)


@auth.route('/my_account', methods=['GET', 'POST'])
@login_required
def my_account():
    if request.method == 'POST':
        recipe_name = request.form.get('recipe_name')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        servings = request.form.get('servings')
        reviews = request.form.get('reviews')
        difficulty = request.form.get('difficulty')

        new_recipe = Recipe(recipe_name=recipe_name, ingredients=ingredients, instructions=instructions,
                            servings=servings, reviews=reviews, difficulty=difficulty, user_id=current_user.id)
        db.session.add(new_recipe)
        r.CSVRecipes(recipe_name, 'image.url', ingredients, instructions, servings, reviews, difficulty)
        flash('Recipe has been added!', category='success')

    return render_template("my_account.html", boolean=True)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password.", category='error')
        else:
            flash('Account does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
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
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created successfully', category='success')
            return redirect(url_for('views.account'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/recipes', methods=['GET'])
@login_required
def recipes():
    all_recipes = r.get_all_recipes()
    return render_template("recipes.html", user=current_user, all_recipes=all_recipes)
