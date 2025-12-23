import os
from flask import Flask
from extensions import db, login_manager
from dotenv import load_dotenv
from os import path

# Load env variables from .env into the system enviornment
load_dotenv()

instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
os.makedirs(instance_path, exist_ok=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(instance_path, "database.db")}'
db.init_app(app)
# --- Blueprint Imports ---
from routes.auth_routes import auth
from routes.view_routes import view

# --- Blueprint Registrations ---
app.register_blueprint(auth)
app.register_blueprint(view)

# Create DBs
with app.app_context():
    db.create_all()
 
if __name__ == '__main__':
    app.run(debug=True)