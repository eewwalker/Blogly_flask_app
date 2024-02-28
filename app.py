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

    users = User.query.all()

    return render_template('homepage.html', users=users)


@app.get("/users/new")
def create_user():

    return render_template('create_user.html')


@app.post("/users/new")
def handle_user():
    first_name = request.form["first_name"]
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

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
