from flask import Flask, Blueprint, request, redirect, url_for, flash, jsonify, render_template
from flask_login import login_required, current_user
from models import Item, List, db
from datetime import datetime

item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/lists/<int:list_id>/create-item', methods=['POST'])
@login_required
def add_item(list_id):
    name = request.form.get('name')
    
    if not name:
        return jsonify({
            'status': 'error',
            'message': 'Item name is required'
        }), 400
    
    # Verify list exists and belongs to user
    parent_list = List.query.filter_by(id=list_id, user_id=current_user.id).first()
    if not parent_list:
        return jsonify({
            'status': 'error',
            'message': 'List not found'
        }), 404
    
    try:
        new_item = Item(
            name=name,
            list_id=list_id
        )
        db.session.add(new_item)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Item created successfully',
            'item': {
                'id': new_item.id,
                'name': new_item.name,
                'created_at': new_item.created_at.isoformat()
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': 'Failed to create item'
        }), 500

@item_bp.route('/lists/<int:list_id>/items/<int:item_id>', methods=['DELETE'])
@login_required
def delete_item(list_id, item_id):
    try:
        # Verify list belongs to user first
        parent_list = List.query.filter_by(id=list_id, user_id=current_user.id).first()
        if not parent_list:
            flash('List not found')
            return redirect(url_for('main_bp.dashboard')), 404
        
        item_to_delete = Item.query.filter_by(id=item_id, list_id=list_id).first()
        if not item_to_delete:
            flash('Item not found')
            return redirect(url_for('main_bp.dashboard')), 404
        
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('Item deleted successfully')
        return redirect(url_for('main_bp.dashboard')), 200
    except Exception as e:
        db.session.rollback()
        flash('Failed to delete item')
        return redirect(url_for('main_bp.dashboard')), 500

@item_bp.route('/lists/<int:list_id>/items/<int:item_id>', methods=['PUT'])
@login_required
def edit_item(list_id, item_id):
    name = request.form.get('name')
    
    if not name:
        flash('Item name is required')
        return redirect(url_for('main_bp.dashboard')), 400
    
    try:
        # Verify list belongs to user first
        parent_list = List.query.filter_by(id=list_id, user_id=current_user.id).first()
        if not parent_list:
            flash('List not found')
            return redirect(url_for('main_bp.dashboard')), 404
        
        item_to_edit = Item.query.filter_by(id=item_id, list_id=list_id).first()
        if not item_to_edit:
            flash('Item not found')
            return redirect(url_for('main_bp.dashboard')), 404
        
        item_to_edit.name = name
        db.session.commit()
        flash('Item updated successfully')
        return redirect(url_for('main_bp.dashboard')), 200
    except Exception as e:
        db.session.rollback()
        flash('Failed to update item')
        return redirect(url_for('main_bp.dashboard')), 500

@item_bp.route('/lists/<int:list_id>/items', methods=['GET'])
@login_required
def get_items(list_id):
    try:
        # Verify list belongs to user first
        parent_list = List.query.filter_by(id=list_id, user_id=current_user.id).first()
        if not parent_list:
            return jsonify({
                'status': 'error',
                'message': 'List not found'
            }), 404
        
        items = Item.query.filter_by(list_id=list_id).all()
        items_data = [{
            'id': item.id,
            'name': item.name,
            'created_at': item.created_at.isoformat()
        } for item in items]
        
        return jsonify({
            'status': 'success',
            'items': items_data
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Failed to fetch items'
        }), 500