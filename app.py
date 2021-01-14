"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

db.create_all()

@app.route("/")
def home_page():
    """Redirects back to users page."""
    return redirect("/users")

@app.route("/users")
def list_users():
    """List users as links to user details"""

    users = User.query.all()
    return render_template("list.html", users=users)

@app.route("/users/new")
def add_user():
    """Gives a form to add a new user"""
    return render_template("new_user_form.html")

@app.route("/users/new", methods=["POST"])
def submit_user():
    """Adds user to db redirect to list."""

    first_name = request.form['first-name']
    last_name = request.form['last-name']
    image_url = request.form['img-url'] 
    image_url = image_url if image_url else None

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show info on a user including name and optional image."""

    user = User.query.get_or_404(user_id) 
    return render_template("user_details.html", user=user)


@app.route("/users/<int:user_id>/edit-user")
def edit_user(user_id):
    """Shows form to edit user details including first and last names, and image"""
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)

@app.route("/users/<int:user_id>/edit-user", methods=["POST"])
def process_edit(user_id):
    """Process the updates to user and redirects to the users list"""
    user = User.query.get_or_404(user_id)

    new_first_name = request.form['first-name']
    new_last_name = request.form['last-name']
    new_image_url = request.form['img-url'] 
    new_image_url = new_image_url if new_image_url else None

    user.first_name=new_first_name
    user.last_name=new_last_name
    user.image_url=new_image_url
    # user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    """Deletes user from the database and returns to the list of users"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/users")

@app.route("/users/<int:user_id>/posts/new")
def add_post_form(user_id):
    """Shows form to add a new post"""
    user = User.query.get_or_404(user_id)
    return render_template("post_form.html", user=user)

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def create_post(user_id):
    """Creates a new post instance upon form submission and redirects to User Details"""
    user = User.query.get_or_404(user_id)
    title=request.form['title']
    content=request.form['content']

    post=Post(title=title, content=content, user_id=user.id)
    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route("/posts/<int:post_id>")
def get_post(post_id):
    post=Post.query.get_or_404(post_id)
    user=post.user #?

    return render_template("post_details.html", post=post, user=user)

@app.route("/posts/<int:post_id>/edit")
def edit_post_form(post_id):
    post=Post.query.get_or_404(post_id)
    user=post.user

    return render_template("edit_post.html", post=post, user=user)

@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def make_post_edit(post_id):
    post = Post.query.get_or_404(post_id)

    new_title = request.form['title']
    new_content = request.form['content']

    post.title=new_title
    post.content=new_content
    
    db.session.add(post)
    db.session.commit()

    return redirect(f"/posts/{post_id}")

@app.route("/posts/<int:post_id>/delete")
def delete_post(post_id):
    """Deletes user from the database and returns to the list of users"""
    post = Post.query.get_or_404(post_id)
    user=post.user
    db.session.delete(post)
    db.session.commit()
    return redirect(f"/users/{user.id}")
