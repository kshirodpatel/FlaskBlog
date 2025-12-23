from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import Post
from extensions import db
view = Blueprint("view", __name__)

@view.route("/")
@view.route("/home")
def home():
    return render_template("home.html")

@view.route("/create-post")
def create_post():
    return render_template("create-post.html")