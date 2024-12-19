from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, UserMixin
from app import db

bp = Blueprint('auth', __name__)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Adicione lógica de autenticação aqui
        pass
    return render_template("login.html")
