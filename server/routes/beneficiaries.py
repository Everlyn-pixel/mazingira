from flask import Blueprint, request, jsonify
from extensions import db
from models.beneficiary import Beneficiary
from flask_jwt_extended import jwt_required, get_jwt_identity

beneficiaries = Blueprint('beneficiaries', __name__, url_prefix='/beneficiaries')

@beneficiaries.route('/', methods=['GET', 'POST'])
@jwt_required()
def handle_beneficiaries():
    current_user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        if not data or not all(key in data for key in ['name', 'organization_id']):
            return jsonify({'error': 'Missing data for beneficiary creation'}), 400
        try:
            new_beneficiary = Beneficiary(name=data['name'], organization_id=data['organization_id'])
            db.session.add(new_beneficiary)
            db.session.commit()
            return jsonify({'message': 'New beneficiary created'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else: # GET request
        try:
            beneficiaries = Beneficiary.query.all()
            return jsonify([{'id': b.id, 'name': b.name, 'organization_id': b.organization_id} for b in beneficiaries]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
