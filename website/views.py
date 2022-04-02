from website import *
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

from website.models import Recipe

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


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





