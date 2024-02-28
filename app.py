"""Blogly application."""

import os

from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User

app = Flask(__name__)

app.config["SECRET_KEY"] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)


@app.get("/")
def redirect_to_homepage():
    return redirect('/users')


@app.get("/users")
def show_homepage():
    return render_template('homepage.html')

@app.get("/users/new")
def create_user():
    return render_template('create_user.html')
#     # show add form
#     # redirect to /users

# @app.post("/users/new")
#     # process add form
#     # add new user
#     # redirect to /users

# @app.get("/users/<int:user_id>")
#     # show info about given user
#     # button here to edit and delete

# @app.get("/users/<int:user_id>/edit")
#     # edit page for user
#     # have cancel button --> redirects to /users/<int:user_id>
#     # save button --> updates user (update db, make sure commit)

# @app.post("/users/<int:user_id>/edit")
#     # process edit form
#     # redirect to /users

# @app.post("/users/<int:user_id>/delete")
    # delete the user
