from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import Post
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
    return render_template("create-post.html")