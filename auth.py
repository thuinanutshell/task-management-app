from flask import Flask, Blueprint, request, redirect, url_for, flash, make_response, render_template
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, db
from datetime import datetime

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    
    # validate required fields
    if not all([email, username, password]):
        flash('All fields are required')
        return redirect(url_for('auth_bp.signup_page'))
    
    user_email = User.query.filter_by(email=email).first()
    user_name = User.query.filter_by(username=username).first()
    
    # check if user exists
    if user_email:
        flash('Email already exists')
        return redirect(url_for('auth_bp.signup_page'))
    
    if user_name:
        flash('Username already exists')
        return redirect(url_for('auth_bp.signup_page'))
    
    try:
        new_user = User(
            email=email,
            username=username,
            password=generate_password_hash(password, method='pbkdf2:sha256'),
            guest=False
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('auth_bp.login_page'))
    except Exception as e:
        db.session.rollback()
        flash('Registration failed')
        return redirect(url_for('auth_bp.signup_page'))

@auth_bp.route('/login', methods=['POST'])
def login():
    identifier = request.form.get('identifier')
    password = request.form.get('password')
    
    if not all([identifier, password]):
        flash('All fields are required')
        return redirect(url_for('auth_bp.login_page'))
    
    user = User.query.filter((User.email == identifier) |
                           (User.username == identifier)).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Invalid credentials')
        return redirect(url_for('auth_bp.login_page'))
    
    login_user(user)
    return redirect(url_for('main_bp.dashboard'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('auth_bp.login_page'))  # Remove the status code

@auth_bp.route('/guest-login')
def guest_login():
    try:
        # Generate unique timestamp
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        guest_username = f"guest_{timestamp}"
        guest_email = f"guest_{timestamp}@temp.com"
        
        guest_user = User(
            username=guest_username,
            email=guest_email,
            password=generate_password_hash('guest'),
            guest=True
        )
        
        db.session.add(guest_user)
        db.session.commit()
        login_user(guest_user)
        return redirect(url_for('main_bp.dashboard'))
        
    except Exception as e:
        db.session.rollback()
        flash('Unable to create guest account. Please try again later.')
        return redirect(url_for('auth_bp.login_page')), 500

@auth_bp.route('/login-page')
def login_page():
    return render_template('auth/login.html')

@auth_bp.route('/signup-page')
def signup_page():
    return render_template('auth/signup.html')