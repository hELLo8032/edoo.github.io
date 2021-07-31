from flask import Blueprint, render_template, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/signup')
def signup(request):
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        psw = request.form['psw']
        psw_repeat = request.form['psw_repeat']
        
        email_valid = False
        try:
            valid = validate_email(email)

            email = valid.email

            email_valid = True
        except EmailNotValidError as e:
            email_valid = False
    
        if psw == psw_repeat:
            if psw is None or len(psw) < 8:
                flash("Passwords should have at least 8 characters!")
            if len(name) =< 1:
                flash("At least 2 characters for the name!")
            if email_valid == False:
                flash("Email not valid!")
            
            user = User(name, email, password, False)

    return render_template("signup.html")

@auth.route('/reset')
def resetpsw():
    return render_template("resetpassword.html")

