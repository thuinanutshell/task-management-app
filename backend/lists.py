from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, Lists

lists = Blueprint('lists', __name__)

@lists.route('/')
def index():
    return render_template("index.html")

@lists.route('/dashboard')
@login_required
def dashboard():
    user_lists = Lists.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", lists=user_lists)

@lists.route('/create_list', methods=['POST'])
@login_required
def create_list():
    list_name = request.form.get('list_name')
    if list_name:
        new_list = Lists(list_name=list_name, user_id=current_user.id)
        db.session.add(new_list)
        db.session.commit()
    return redirect(url_for('lists.dashboard'))

@lists.route('/edit_list/<int:list_id>', methods=['GET', 'POST'])
@login_required
def edit_list(list_id):
    list_item = Lists.query.get_or_404(list_id)
    if request.method == 'POST':
        list_item.list_name = request.form.get('list_name')
        db.session.commit()
        return redirect(url_for('lists.dashboard'))
    return render_template('edit_list.html', list=list_item)

@lists.route('/delete_list/<int:list_id>')
@login_required
def delete_list(list_id):
    list_item = Lists.query.get_or_404(list_id)
    if list_item.user_id == current_user.id:
        db.session.delete(list_item)
        db.session.commit()
    return redirect(url_for('lists.dashboard'))

@lists.route('/view_list/<int:list_id>')
@login_required
def view_list(list_id):
    list_item = Lists.query.get_or_404(list_id)
    return render_template('view_list.html', list=list_item)

@lists.route('/profile')
def profile():
    return render_template("profile.html")