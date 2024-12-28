from flask import Blueprint, render_template
from models import db, Lists

lists = Blueprint('lists', __name__)

@lists.route('/')
def index():
    return render_template("index.html")

@lists.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@lists.route('/profile')
def profile():
    return render_template("profile.html")