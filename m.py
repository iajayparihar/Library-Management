from db import db
from datetime import date
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_enc = db.Column(db.String(50), unique=False, nullable=False)
    address = db.Column(db.String(20))
    country = db.Column(db.String(20))
    users = db.relationship('Borrow', backref='user', lazy=True)

    def __init__(self, user_name, phone, email, password_enc, address, country):
        self.user_name = user_name
        self.phone = phone
        self.email = email
        self.password_enc = password_enc
        self.address = address
        self.country = country

    # Uncomment these methods if you plan to use password hashing
    # def set_password(self, password):
    #     self.password_enc = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_enc, password)

    def __repr__(self):
        return f"User: {self.user_name}, Email: {self.email}"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    author = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default="Available")  # Use a more descriptive status field
    books = db.relationship('Borrow', backref='book', lazy=True)

    def __init__(self, title, author, description, status):
        self.title = title
        self.author = author
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Book: {self.title}, Author: {self.author}"

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrow_date = db.Column(db.Date, default=date.today(), nullable=False)
    return_date = db.Column(db.Date)

    def __repr__(self):
        return f"User ID: {self.user_id}, Book ID: {self.book_id}, Borrowed on: {self.borrow_date}"
