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
@login_required
def dashboard():
    books = Book.query.all()
    borrow = Borrow.query.all()
    return render_template('dashboard.html', books = books, borrow = borrow )

@app.route('/returnBook/<int:b_id>/<int:book_id>',methods=["GET","POST"])
@login_required
def returnBook(b_id,book_id):
    # change in book status unAvailable to Available in book table
    book = Book.query.get(book_id)
    book.status = "Available"
    
    # in the borrow table return_date feed
    bor = Borrow.query.get(b_id)
    bor.return_date = date.today()

    db.session.add_all([book,bor])
    db.session.commit()
    return redirect(url_for('dashboard'))    

@app.route('/borrow/<int:user_id>/<int:book_id>')
@login_required
def borrow(user_id,book_id):
    user = User.query.get(user_id) 
    book = Book.query.get(book_id)
    if (user or book) is None:
        flash(f'some error occur sorry!','danger')
        return redirect(url_for('dashboard'))

    if book.status == "Available":
        bor = Borrow(user_id=user_id,book_id=book_id)
        db.session.add(bor)
        db.session.commit()
        
        book.status = "Unavailable"
        db.session.add(book)
        db.session.commit()
        flash(f'Successfully borrowed !!','success')
    else:
        flash(f'Book is not Available','warning')

    return redirect(url_for('dashboard'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

            # walrus operator :=
        if user := User.query.filter_by(username=username, password=password).first():
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash(f"Enter the currect username or Password.",category="danger")
        
    return render_template('login.html')

@app.route('/logout',methods=['GET',"POST"])
def logout():
    logout_user()
    return redirect(url_for('login'))


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