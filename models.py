from db import db
from datetime import date
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique = False, nullable = False)
    phone = db.Column(db.String(20), unique = False, nullable = False)
    email = db.Column(db.String(100), unique = True , nullable = False )
    password_enc = db.Column(db.String(50), unique = False , nullable = False)
    address = db.Column(db.String(20))
    country = db.Column(db.String(20))
    users = db.relationship('Borrow',backref='user',lazy=True)
	
    book = db.relationship('Book',backref='user',lazy=True)
    
    def __init__(self,user_name,phone,email,password_enc,address,country):
        self.user_name = user_name
        self.phone = phone
        self.email = email
        self.password_enc = password_enc
        self.address = address
        self.country = country
        

    # def set_password(self,password):
    #     self.password_enc = generate_password_hash(password)

    # def check_password(self,password):
	# 								# saved pass,   given pass
    #     return check_password_hash(self.password_enc,password)

    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    title = db.Column(db.String(50),unique = False , nullable = False)
    author = db.Column(db.String(50),unique = False , nullable = False )
    description = db.Column(db.Text)
    status = db.Column(db.Boolean,default=True)
    books = db.relationship('Borrow',backref='book',lazy=True)

    def __init__(self, title, author, description, status):
        self.title = title
        self.author = author
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Title : {self.title}, author: {self.author}"

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)
    book_id = db.Column(db.Integer,db.ForeignKey('book.id'), nullable = False)
    borrow_date = db.Column(db.Date, unique = False , nullable = False)

    def __repr__(self):
        return f"user_id : {self.user_id}, book_id: {self.book_id}"
