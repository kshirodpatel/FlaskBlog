from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import Post, User
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db
post = Blueprint("post", __name__)

@post.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == 'POST':
        post_title = request.form.get("title")
        post_content = request.form.get("description")
        post_category = request.form.get("category")

        if len(post_title) < 5 or len(post_content) < 5 :
            print("Post title and Content should be more than 5 characters")
        else :
            new_post = Post(post_title=post_title, post_content=post_content, post_category=post_category, author=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            print("Post created")
            return redirect(url_for("post.create_post"))
    return render_template("/post/create-post.html")

@post.route("/post/<post_id>", methods=["GET", "POST"])
@login_required
def post_view(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return render_template("error.html", post_id=post_id)
    else:
        return render_template("/post/post-details.html", post_id=post_id)

@post.route("/posts/<author_name>", methods=["GET", "POST"])
@login_required
def posts_by_author(author_name):
    user = User.query.filter_by(username=author_name).first()
    if not user:
        return render_template("error.html", post_id=author_name)
    else:
        return render_template("/author/posts-by-author.html", author=author_name)  