from flask import Flask
from flask_login import UserMixin
from sqlalchemy import Column, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    guest = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    
    # one-to-many relationship with list
    # backref indicates the bidirectional relationship between two tables
    # cascade automatically delete child records if the parent's record is deleted
    lists = relationship('List', backref='owner', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"

class List(db.Model):
    __tablename__ = 'lists'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    
    # One-to-many relationship with user's table
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    items = relationship('Item', backref='list', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"List(name={self.name}, user_id={self.user_id})"
    
class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    
    # one-to-many relationship with the list table
    list_id = db.Column(db.Integer, ForeignKey('lists.id'), nullable=False)
    
    def __repr__(self):
        return f"Item(name={self.name}, list_id={self.list_id})"

