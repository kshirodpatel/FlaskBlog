from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import Post
view = Blueprint("view", __name__)

@view.route("/")
@view.route("/home")
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts)