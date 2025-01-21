from flask import Flask
from flask_login import LoginManager
from models import db, User
from auth import auth as auth_bp
from lists import lists as lists_bp
from items import items as items_bp
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp)
app.register_blueprint(lists_bp)
app.register_blueprint(items_bp)

if __name__ == '__main__':
    app.run(debug=True)