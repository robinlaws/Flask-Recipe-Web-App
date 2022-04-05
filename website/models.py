from website import *
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(10000))
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

    def __init__(self, email, first_name, password):
        self.email = email
        self.first_name = first_name
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)





