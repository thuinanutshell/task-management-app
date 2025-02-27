from flask import Flask, Blueprint, request, redirect, url_for, flash, jsonify, render_template
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import List, db
from datetime import datetime

list_bp = Blueprint('list_bp', __name__)

@list_bp.route('/create-list', methods=['POST'])
@login_required
def add_list():
    name = request.form.get('name')
    
    if not name:
        if request.headers.get('Accept') == 'application/json':
            return jsonify({'status': 'error', 'message': 'List name is required'}), 400
        flash('List name is required')
        return render_template('dashboard.html', user=current_user), 400
    
    try:
        new_list = List(
            name=name,
            user_id=current_user.id
        )
        db.session.add(new_list)
        db.session.commit()

        if request.headers.get('Accept') == 'application/json':
            return jsonify({
                'status': 'success',
                'message': 'List created successfully',
                'list': {
                    'id': new_list.id,
                    'name': new_list.name,
                    'created_at': new_list.created_at.isoformat()
                }
            }), 201

        flash('Successfully created a list')
        user_lists = List.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', lists=user_lists, user=current_user), 201

    except Exception as e:
        db.session.rollback()
        if request.headers.get('Accept') == 'application/json':
            return jsonify({'status': 'error', 'message': 'Failed to create list'}), 500
        flash('Failed to create list')
        return render_template('dashboard.html', user=current_user), 500

@list_bp.route('/delete-list/<int:list_id>', methods=['DELETE'])
@login_required
def delete_list(list_id):
    try:
        list_to_delete = List.query.filter_by(
            id=list_id, 
            user_id=current_user.id
        ).first()
        
        if not list_to_delete:
            flash('List not found')
            return redirect(url_for('main_bp.dashboard')), 404
        
        db.session.delete(list_to_delete)
        db.session.commit()
        flash('List deleted successfully')
        return redirect(url_for('main_bp.dashboard')), 200
    except Exception as e:
        db.session.rollback()
        flash('Failed to delete list')
        return redirect(url_for('main_bp.dashboard')), 500

@list_bp.route('/edit-list/<int:list_id>', methods=['PUT'])
@login_required
def edit_list(list_id):
    name = request.form.get('name')
    
    if not name:
        flash('List name is required')
        return redirect(url_for('main_bp.dashboard')), 400
    
    try:
        list_to_edit = List.query.filter_by(
            id=list_id, 
            user_id=current_user.id
        ).first()
        
        if not list_to_edit:
            flash('List not found')
            return redirect(url_for('main_bp.dashboard')), 404
        
        list_to_edit.name = name
        db.session.commit()
        flash('List updated successfully')
        return redirect(url_for('main_bp.dashboard')), 200
    except Exception as e:
        db.session.rollback()
        flash('Failed to update list')
        return redirect(url_for('main_bp.dashboard')), 500

@list_bp.route('/get-lists', methods=['GET'])
@login_required
def get_lists():
    try:
        user_lists = List.query.filter_by(user_id=current_user.id).all()
        lists_data = [{
            'id': lst.id,
            'name': lst.name,
            'created_at': lst.created_at.isoformat()
        } for lst in user_lists]
        
        return jsonify({
            'status': 'success',
            'lists': lists_data
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Failed to fetch lists'
        }), 500
