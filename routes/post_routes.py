from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import Post, User, Comment
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db
from sqlalchemy.sql import func
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
    current_post = Post.query.filter_by(id=post_id).first()
    if current_post is None:
        return render_template("error.html", post_id=post_id)
    else:
        random_posts = Post.query.filter(id != post_id).order_by(func.random()).limit(2).all()

        if request.method == "POST":
            post_comment = request.form.get("post_comment")

            if len(post_comment) < 5 :
                post_comments = Comment.query.filter_by(
        post_id=post_id).all()
                return render_template("/post/post-details.html", post=current_post, random_posts = random_posts, post_comments=post_comments)

            new_comment = Comment(text=post_comment, author=current_user.id, post_id=post_id)
            print("New comment added")
            db.session.add(new_comment)
            db.session.commit()

        post_comments = Comment.query.filter_by(post_id=post_id).all()
        return render_template("/post/post-details.html", post=current_post, random_posts = random_posts, post_comments=post_comments, author=current_user.id)

    

@post.route("/posts/<author_name>", methods=["GET", "POST"])
@login_required
def posts_by_author(author_name):
    user = User.query.filter_by(username=author_name).first()
    if not user:
        return render_template("error.html", post_id=author_name)
    else:
        posts = user.posts
        return render_template("/author/posts-by-author.html", posts=posts)  