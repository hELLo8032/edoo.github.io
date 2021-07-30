from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    pass

@views.route('/home')
def logged_in():
    pass
