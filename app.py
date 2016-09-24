from flask import Flask, g, redirect
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager

import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'
MONGODB_NAME = 'microflask'

app = Flask(__name__)
app.secret_key = 'somerandomsupersecret-strings!'
app.config['MONGODB_SETTINGS'] = {'DB': MONGODB_NAME}

# Setting up the DB
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userId):
    if userId is None:
        redirect('/login')
    user = User()
    user.get_by_id(userId)

    if user.is_active():
        return user
    else:
        return None

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
