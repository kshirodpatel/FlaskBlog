import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '@#4%#$FgVBX&>?&*#$'

# --- Blueprint Imports ---
from routes.auth_routes import auth

# --- Blueprint Registrations ---
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)