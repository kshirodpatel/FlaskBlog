from extensions import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    phone = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(150))
    # date_created = db.Column(db.dateTime(timezone=True), default=func.now())

# class Post(db.Model):
#     id: db.Column(db.Integer, primary_key=True)
#     post_title: db.Column(db.String(150))
#     post_content: db.Column(db.Text, nullable=False)
#     # date_created: db.Column(db.DateTime(timezone=True), default=func.now())
#     author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False) 