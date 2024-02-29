"""Blogly application."""

import os

from flask import Flask, request, render_template, redirect
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Post

app = Flask(__name__)

app.config["SECRET_KEY"] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# debug = DebugToolbarExtension(app)
connect_db(app)


@app.get("/")
def redirect_to_homepage():
    """ Redirect to homepage"""

    return redirect('/users')


@app.get("/users")
def show_homepage():
    """ Renders homepage HTML with users """

    users = User.query.all()

    return render_template('homepage.html', users=users)


@app.get("/users/new")
def create_user():
    """ Renders new user form """

    return render_template('create_user.html')


@app.post("/users/new")
def handle_user():
    """ Handles new user form post request """
    first_name = request.form["first_name"]
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    new_user = User(
        first_name=first_name,
        last_name=last_name,
        image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.get("/users/<int:user_id>")
def show_user(user_id):
    """ Rendered user details HTML page """
    user = User.query.get_or_404(user_id)
    return render_template(
        'user_details.html',
        user=user)


@app.get("/users/<int:user_id>/edit")
def show_edit(user_id):
    """ Rendered edit page for user """
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html',
                           user=user)


@app.post("/users/<int:user_id>/edit")
def edit_user(user_id):
    """ Handles edit user form and redirect to users """
    first_name = request.form["first_name"]
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User.query.get_or_404(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.commit()
    return redirect('/users')


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """ Handles delete user and redirect to users page """
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')

# routes for the posts


@app.get("/users/<int:user_id>/posts/new")
def show_post_form(user_id):
    return render_template('new_post.html')


@app.post("/users/<int:user_id>/posts/new")
def handle_add_form(user_id):

    title = request.form["title"]
    content = request.form["content"]

    post = Post(
        title=title,
        content=content,
        user_id=user_id
        )

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.get("/posts/<int:post_id>")
def show_post(post_id):

    post = Post.query.get_or_404(post_id)

     #show post
     #edit post button
     #delete post button
    return render_template("post_detail.html", post=post)

# @app.get("/posts/<int:post_id>/edit")
# def edit_post_form(post_id):
#     #show form
#     #edit button
#     #cancel redirects to user page

# @app.post("/posts/<int:post_id>/edit")
# def handle_edit_form(post_id):
#     #redirect to post vieew /posts/<int:post_id>

# @app.post("/posts/<post_id>/delete")
# def delete_post(post_id):
