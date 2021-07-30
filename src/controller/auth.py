from flask import Blueprint, render_template
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/reset')
def resetpsw():
    return render_template("resetpassword.html")

