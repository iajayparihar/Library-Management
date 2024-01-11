from db import app,db
# import init
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from models import *
from flask import render_template, request, redirect , url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user,UserMixin

login_manager = LoginManager()
login_manager.init_app(app)

# Creating an SQLAlchemy instance
with app.app_context():
	db.create_all()

@login_manager.user_loader
def load_user(user_id):
    # Load a user by their user_id (typically from a database) """they hole the current logged user id"""
    return User.query.get(int(user_id))


@app.route('/dashboard', methods=['GET','POST'])
def dashborad():
    books = Book.query.all()
    return render_template('dashboard.html',books = books)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

            # walrus operator :=
        if user := User.query.filter_by(username=username, password=password).first():
            login_user(user)
            return redirect(url_for('dashborad'))
        
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def registration():
    if request.method != 'POST':
        return render_template('registration.html', title='Register')
    username = request.form['username']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']
    address = request.form['address']
    country = request.form['country']

    # check if the user already exist , then redirect to the login page witha a message you already have a account
    
    # if user does not have a account then access to create a new account

    if new_user := User(username=username,\
                        phone=phone,\
                        email=email,\
                        password=password,\
                        address=address,\
                        country=country):

        db.session.add(new_user)
        db.session.commit()
    else:
        flash(f'Account creation Fail !!', 'error')
        return redirect(url_for('register'))

    flash(f'Account created for {username}.', 'success')
    return redirect(url_for('login'))



if __name__ == '__main__':
	app.run(debug=True)


# from app import app, db
# app.app_context().push()
# db.create_all()

# <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">