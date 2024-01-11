# import init
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from models import *
from flask import render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user,UserMixin
from db import app,db

login_manager = LoginManager()
login_manager.init_app(app)

# Creating an SQLAlchemy instance
with app.app_context():
	db.create_all()

@login_manager.user_loader
def load_user(user_id):
    # Load a user by their user_id (typically from a database) """they hole the current logged user id"""
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def registration():
	return render_template('registration.html')

if __name__ == '__main__':
	app.run(debug=True)


# from app import app, db
# app.app_context().push()
# db.create_all()

# <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">