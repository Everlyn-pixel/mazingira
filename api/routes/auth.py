from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not all(key in data for key in ['username', 'email', 'password', 'role']):
        return jsonify({'error': 'Missing data'}), 400
    try:
        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password, role=data['role'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'New user created!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not all(key in data for key in ['username', 'password']):
        return jsonify({'error': 'Missing data'}), 400
    try:
        user = User.query.filter_by(username=data['username']).first()
        if not user or not check_password_hash(user.password_hash, data['password']):
            return jsonify({'message': 'Bad username or password'}), 401
        
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
