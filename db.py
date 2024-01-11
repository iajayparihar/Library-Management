from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLACHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'your_secret_key'
db = SQLAlchemy(app=app)
migra = Migrate(app,db)