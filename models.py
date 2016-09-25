import datetime

from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from app import app, db


flask_bcrypt = Bcrypt(app)

class User(db.Document, UserMixin):
    username = db.StringField(default=True)
    email = db.EmailField(unique=True)
    password = db.StringField(default=True)
    is_active = db.BooleanField(default=True)
    is_admin = db.BooleanField(default=False)
    created_at = db.DateTimeField(default=datetime.datetime.now())

class Status(db.Document):
    text = db.StringField(default=True)
    created_at = db.DateTimeField(default=datetime.datetime.now())

def initialize():
    # if there is no data, insert one

    if User.objects.count() < 1:
        user = User(username='admin', email='email@microflask.com', password=flask_bcrypt.generate_password_hash('admin'), is_admin=True)
        user.save()
    return None

