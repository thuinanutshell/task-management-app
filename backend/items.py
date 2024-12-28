from flask import Blueprint, render_template
from models import db, Items

items = Blueprint('items', __name__)
