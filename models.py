import datetime

from flask_login import UserMixin
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from app import app

db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

class User(db.Document):
    username = db.StringField(default=True)
    email = db.EmailField(unique=True)
    password = db.StringField(default=True)
    active = db.BooleanField(default=True)
    isAdmin = db.BooleanField(default=False)
    createdAt = db.DateTimeField(default=datetime.datetime.now())
