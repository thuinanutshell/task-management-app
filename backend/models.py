from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hashed = db.Column(db.String(80))
    
    lists = db.relationship("Lists", back_populates="user", lazy="dynamic")
    
class Lists(db.Model):
    __tablename__="lists"
    
    id = db.Column(db.Integer, primary_key=True)
    list_name=db.Column(db.String(80), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="lists")
    items = db.relationship("Items", back_populates="lst", lazy="dynamic")

class Items(db.Model):
    __tablename__="items"
    
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String, nullable=False)
    
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"), nullable=False)
    lst = db.relationship("Lists", back_populates="lists")