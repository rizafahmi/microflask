import datetime

from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from app import app, db


flask_bcrypt = Bcrypt(app)

class User(db.Document, UserMixin):
    username = db.StringField(min_length=4, max_length=75)
    email = db.StringField(required=True)
    password = db.StringField(required=True, min_length=4)
    is_active = db.BoolField(default=True)
    is_admin = db.BoolField(default=True)
    created_at = db.DateTimeField(default=datetime.datetime.now())

class Status(db.Document):
    text = db.StringField()
    created_at = db.DateTimeField(default=datetime.datetime.now())

def initialize():
    # if there is no data, insert one

    if len(User.query.all()) < 1:
        user = User(username='admin', email='email@microflask.com', password=flask_bcrypt.generate_password_hash('admin').decode(), is_admin=True)
        user.save()
