from flask import (
        Flask,
        g,
        redirect,
        render_template,
        flash,
        url_for
        )
from flask_login import LoginManager, login_user
from flask_bcrypt import Bcrypt, check_password_hash
from flask_mongoalchemy import MongoAlchemy

import models
import forms

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'
MONGODB_NAME = 'microflask'

app = Flask(__name__)
app.secret_key = 'somerandomsupersecret-strings!'
app.config['MONGOALCHEMY_DATABASE'] = MONGODB_NAME

# Setting up the DB
db = MongoAlchemy(app)

flask_bcrypt = Bcrypt(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userId):
    if userId is None:
        redirect('/login')
    user = models.User.objects.with_id(userId)

    import ipdb;ipdb.set_trace()
    if user.is_active:
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
            flash("Unable to register.", "error")
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():

        try:
            # import ipdb;ipdb.set_trace()
            user = models.User.one(email=form.email.data)
        except DoesNotExist:
            print("Your email or password doesn't match!")
        else:
            if flask_bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You've been logged in!")
                return redirect(url_for('index'))
            else:
                flash("Your email or password doesn't match!", "error")
    return render_template('login.html', form=form)


@app.route('/')
def index():
    flash('hey', 'success')
    return 'Hey'


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
