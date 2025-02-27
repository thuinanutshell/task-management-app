from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import List

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    user_lists = List.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', lists=user_lists, user=current_user)
