from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (
        DataRequired,
        Regexp,
        ValidationError,
        Email,
        EqualTo,
        Length
        )

import models


def name_exists(form, field):
    if models.User.objects(username=field.data).count() > 0:
        return ValidationError('User with that username already exists.')

def email_exists(form, field):
    if models.User.objects(email=field.data).count() > 0:
        return ValidationError('User with that email already exists.')

class RegisterForm(Form):
    username = StringField(
            'Username',
            validators=[
                DataRequired(),
                Regexp(
                    r'^[a-zA-Z0-9_]+$',
                    message=("Username should be one word, letters, "
                        "numbers, and underscores only."
                        )
                    ),
                name_exists
                ])
    email = StringField(
            'Email',
            validators=[
                DataRequired(),
                Email(),
                email_exists
                ])

    password = PasswordField(
            'Password',
            validators=[
                DataRequired(),
                Length(min=2),
                EqualTo('password2', message='Password must match.')
                ])
    password2 = PasswordField(
            'Confirm Password',
            validators=[DataRequired()]
            )

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
