from flask import Blueprint, request, jsonify
from extensions import db
from models.beneficiary import Beneficiary

beneficiaries = Blueprint('beneficiaries', __name__, url_prefix='/beneficiaries')

@beneficiaries.route('/', methods=['GET', 'POST'])
def handle_beneficiaries():
    if request.method == 'POST':
        data = request.get_json()
        new_beneficiary = Beneficiary(name=data['name'], organization_id=data['organization_id'])
        db.session.add(new_beneficiary)
        db.session.commit()
        return jsonify({'message': 'New beneficiary created!'})
    else:
        beneficiaries = Beneficiary.query.all()
        return jsonify([{'name': b.name, 'organization_id': b.organization_id} for b in beneficiaries])
