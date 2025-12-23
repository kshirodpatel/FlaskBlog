from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from extensions import db
auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form.get('firstname').strip()
        lastname = request.form.get('lastname').strip()
        phone = request.form.get('phone').strip()
        email = request.form.get('email').strip()
        password = request.form.get('password').strip()
        confirm_password = request.form.get('confirm_password').strip()

        user = User.query.filter_by(email=email).first()
        if user:
            print('User already exists')
        else :
            if len(email) < 4:
                flash("Email is too short", category="error")
            elif len(firstname) < 3 or len(lastname) < 3 :
                flash("Firstname and Lastname should be more than 3 characters", category="error")
            elif password != confirm_password:
                flash("Password and Confirm Password should be same", category="error")
            elif len(password) < 7:
                flash("Password is less than 7 character", category="error")
            else:
                # Create User
                print("Create User")
                new_user = User(email=email, firstname=firstname, lastname=lastname, phone=phone, password=generate_password_hash(password, method="scrypt", salt_length=16))
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("view.home"))
    return render_template("signup.html")

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("/profile")
def profile():
    return render_template("profile.html")