from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    image_url = db.Column(db.String(1000))
    ingredients = db.Column(db.String(1000))
    instructions = db.Column(db.String(1000))
    servings = db.Column(db.String(1000))
    reviews = db.Column(db.String(1000))
    difficulty = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    recipes = db.relationship('Recipe')



