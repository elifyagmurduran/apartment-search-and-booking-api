from flask import Blueprint, request, jsonify
from .models import Apartment
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

apartments_bp = Blueprint('apartments', __name__)

@apartments_bp.route('/add', methods=['POST'])
def add_apartment():
    # Implement the logic to add an apartment
    pass

@apartments_bp.route('/remove', methods=['DELETE'])
def remove_apartment():
    # Implement the logic to remove an apartment
    pass

@apartments_bp.route('/list', methods=['GET'])
def list_apartments():
    # Implement the logic to list all apartments
    pass
