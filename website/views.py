from website import *
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

from website.models import Recipe

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
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
        flash('Recipe has been added!', category='success')


    return render_template("home.html", boolean=True)


@views.route('/recipes')
def recipes():
    return render_template("recipes.html")



@views.route('/delete-recipe', methods=['POST'])
def delete_recipe():
    recipe = json.loads(request.data)
    recipe_id = recipe['recipeID']
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        if recipe.user_id == current_user.id:
            db.session.delete(recipe)
            db.session.commit()

    return jsonify({})





