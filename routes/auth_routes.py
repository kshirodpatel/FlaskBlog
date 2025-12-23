from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db

auth = Blueprint("auth", __name__)

# Route for login user
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for("view.home"))
            else:
                print("Invalid password")
        else:
            print("Invalid User")
    return render_template("login.html", user=current_user)

# Route for signup user
@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email').strip()
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        confirm_password = request.form.get('confirm_password').strip()

        user = User.query.filter_by(email=email).first()
        if user:
            print('User already exists.')
        else :
            if len(email) < 4:
                flash("Email is too short", category="error")
            elif password != confirm_password:
                flash("Password and Confirm Password should be same", category="error")
            elif len(password) < 7:
                flash("Password is less than 7 character", category="error")
            else:
                # Create User
                print("Create User")
                new_user = User(email=email, username=username, password=generate_password_hash(password, method="scrypt", salt_length=16))
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("auth.login"))
    return render_template("signup.html", user=current_user)

# Route for Logout
@auth.route("/logout")
def logout():
    return render_template("home.html")

# Route for user profile
@auth.route("/profile")
def profile():
    return render_template("profile.html", user=current_user)

# Route for user logout
@auth.route("/sign-out")
@login_required
def sign_out():
    logout_user()
    return redirect(url_for("auth.login"))