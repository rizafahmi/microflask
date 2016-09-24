from flask import (
        Flask,
        g,
        redirect,
        render_template,
        flash,
        url_for
        )
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

import models
import forms

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

flask_bcrypt = Bcrypt(app)

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")
        username = form.username.data
        email = form.email.data
        password = flask_bcrypt.generate_password_hash(form.password.data)
        user = models.User(
                username=username,
                email=email,
                password=password)

        try:
            user.save()
            return redirect(url_for('index'))
        except:
            flash("Unable to register.")
    return render_template('register.html', form=form)

@app.route('/')
def index():
    return 'Hey'


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
