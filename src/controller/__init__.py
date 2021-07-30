from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Fenerbahce17"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    import .models

    create_database(app)

    return app

def create_database(app):
    if not path('devtools/' + DB_NAME):
        db.create_all(app=app)
        print("DATABASE CREATED")