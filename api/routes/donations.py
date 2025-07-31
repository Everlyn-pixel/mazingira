from flask import Blueprint, request, jsonify
from extensions import db
from models.donation import Donation
from flask_jwt_extended import jwt_required, get_jwt_identity

donations = Blueprint('donations', __name__)

@donations.route('/', methods=['POST'])
@jwt_required()
def create_donation():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    if not data or not all(key in data for key in ['amount', 'organization_id', 'donation_type']):
        return jsonify({'error': 'Missing data for donation creation'}), 400
    try:
        new_donation = Donation(
            amount=data['amount'],
            donor_id=current_user_id,
            organization_id=data['organization_id'],
            is_anonymous=data.get('is_anonymous', False),
            donation_type=data['donation_type']
        )
        db.session.add(new_donation)
        db.session.commit()
        return jsonify({'message': 'Donation created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
