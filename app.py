import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
DB_NAME = 'database.db'
app.config['SECRET_KEY'] = '@#4%#$FgVBX&>?&*#$'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"

# --- Blueprint Imports ---
from routes.auth_routes import auth
from routes.view_routes import view

# --- Blueprint Registrations ---
app.register_blueprint(auth)
app.register_blueprint(view)

if __name__ == '__main__':
    app.run(debug=True)