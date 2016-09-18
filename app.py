from flask import (
Flask, request, session, g, redirect,
url_for, abort, render_template, flash
        )
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Halo, Bandung!"


if __name__ == '__main__':
    app.run()
