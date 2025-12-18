from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "@#4%#$FgVBX&>?&*#$"

    from .views import views
    from .auth import auth
