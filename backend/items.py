from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, Items, Lists

items = Blueprint('items', __name__)

@items.route('/add_item/<int:list_id>', methods=['GET', 'POST'])
@login_required
def add_item(list_id):
    list_item = Lists.query.get_or_404(list_id)
    if request.method == 'POST':
        item_name = request.form.get('item_name')
        if item_name:
            new_item = Items(item_name=item_name, list_id=list_id)
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('lists.view_list', list_id=list_id))
    return render_template('add_item.html', list=list_item)

@items.route('/toggle_item', methods=['POST'])
@login_required
def toggle_item():
    item_id = request.form.get('item_id')
    if item_id:
        item = Items.query.get_or_404(item_id)
        item.is_completed = not item.is_completed
        db.session.commit()
    return redirect(url_for('lists.dashboard'))
