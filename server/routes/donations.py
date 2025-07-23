from flask import Blueprint, request, jsonify
from extensions import db
from models.donation import Donation

donations = Blueprint('donations', __name__, url_prefix='/donations')

@donations.route('/', methods=['POST'])
def create_donation():
    data = request.get_json()
    new_donation = Donation(
        amount=data['amount'],
        donor_id=data['donor_id'],
        organization_id=data['organization_id'],
        is_anonymous=data.get('is_anonymous', False),
        donation_type=data['donation_type']
    )
    db.session.add(new_donation)
    db.session.commit()
    return jsonify({'message': 'Donation created successfully!'}), 201
