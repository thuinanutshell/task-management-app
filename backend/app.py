from flask import Flask
from models import db
from auth import auth as auth_bp
from lists import lists as lists_bp
from items import items as items_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(lists_bp)
app.register_blueprint(items_bp)

if __name__ == '__main__':
    app.run(debug=True)