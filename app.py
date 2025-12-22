import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from os import path

# Load env variables from .env into the system enviornment
load_dotenv()

app = Flask(__name__)
DB_NAME = os.environ.get('DB_NAME')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"

# --- Blueprint Imports ---
from routes.auth_routes import auth
from routes.view_routes import view

# --- Blueprint Registrations ---
app.register_blueprint(auth)
app.register_blueprint(view)

if __name__ == '__main__':
    app.run(debug=True)