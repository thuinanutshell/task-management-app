from flask import Flask, Blueprint, redirect, url_for
import os
from dotenv import load_dotenv
from flask_login import LoginManager
from models import db, User
from lists import list_bp
from items import item_bp
from auth import auth_bp
from main import main_bp

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure app
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")  # Required for session management
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_bp.login_page'

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(list_bp)
app.register_blueprint(item_bp)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)