from flask import Blueprint, request, jsonify
from extensions import db
from models.organization import Organization

organizations = Blueprint('organizations', __name__, url_prefix='/organizations')

@organizations.route('/', methods=['GET', 'POST'])
def handle_organizations():
    if request.method == 'POST':
        data = request.get_json()
        new_organization = Organization(name=data['name'], description=data['description'], user_id=data['user_id'])
        db.session.add(new_organization)
        db.session.commit()
        return jsonify({'message': 'New organization created!'})
    else:
        organizations = Organization.query.all()
        return jsonify([{'name': org.name, 'description': org.description, 'status': org.status} for org in organizations])

@organizations.route('/<int:id>/approve', methods=['PUT'])
def approve_organization(id):
    organization = Organization.query.get_or_404(id)
    organization.status = 'approved'
    db.session.commit()
    return jsonify({'message': 'Organization approved!'})

@organizations.route('/<int:id>/reject', methods=['PUT'])
def reject_organization(id):
    organization = Organization.query.get_or_404(id)
    organization.status = 'rejected'
    db.session.commit()
    return jsonify({'message': 'Organization rejected!'})

@organizations.route('/<int:id>', methods=['PUT'])
def update_organization(id):
    organization = Organization.query.get_or_404(id)
    data = request.get_json()
    organization.name = data.get('name', organization.name)
    organization.description = data.get('description', organization.description)
    db.session.commit()
    return jsonify({'message': 'Organization updated!'})

@organizations.route('/<int:id>', methods=['DELETE'])
def delete_organization(id):
    organization = Organization.query.get_or_404(id)
    db.session.delete(organization)
    db.session.commit()
    return jsonify({'message': 'Organization deleted!'})

@organizations.route('/<int:id>/donations', methods=['GET'])
def get_organization_donations(id):
    organization = Organization.query.get_or_404(id)
    donations = organization.donations
    total_donations = sum(d.amount for d in donations)
    non_anonymous_donations = [{'donor': d.donor.username, 'amount': d.amount} for d in donations if not d.is_anonymous]
    anonymous_donations = sum(d.amount for d in donations if d.is_anonymous)
    return jsonify({
        'total_donations': total_donations,
        'non_anonymous_donations': non_anonymous_donations,
        'anonymous_donations_total': anonymous_donations
    })
