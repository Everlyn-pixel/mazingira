from flask import Blueprint, request, jsonify
from extensions import db
from models.organization import Organization
from models.donation import Donation # Import Donation model for relationships
from models.user import User # Import User model for relationships
from flask_jwt_extended import jwt_required, get_jwt_identity

organizations = Blueprint('organizations', __name__, url_prefix='/organizations')

@organizations.route('/', methods=['GET', 'POST'])
@jwt_required()
def handle_organizations():
    current_user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        if not data or not all(key in data for key in ['name', 'description']):
            return jsonify({'error': 'Missing data for organization creation'}), 400
        try:
            new_organization = Organization(name=data['name'], description=data['description'], user_id=current_user_id)
            db.session.add(new_organization)
            db.session.commit()
            return jsonify({'message': 'New organization created!'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else: # GET request
        try:
            organizations = Organization.query.all()
            return jsonify([{'id': org.id, 'name': org.name, 'description': org.description, 'status': org.status, 'user_id': org.user_id} for org in organizations]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@organizations.route('/<int:id>/approve', methods=['PUT'])
@jwt_required()
def approve_organization(id):
    # Add role-based access control here if needed (e.g., only admin can approve)
    try:
        organization = Organization.query.get_or_404(id)
        organization.status = 'approved'
        db.session.commit()
        return jsonify({'message': 'Organization approved!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@organizations.route('/<int:id>/reject', methods=['PUT'])
@jwt_required()
def reject_organization(id):
    # Add role-based access control here if needed (e.g., only admin can reject)
    try:
        organization = Organization.query.get_or_404(id)
        organization.status = 'rejected'
        db.session.commit()
        return jsonify({'message': 'Organization rejected!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@organizations.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_organization(id):
    # Add role-based access control here if needed (e.g., only organization owner can update)
    try:
        organization = Organization.query.get_or_404(id)
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided for update'}), 400
        organization.name = data.get('name', organization.name)
        organization.description = data.get('description', organization.description)
        db.session.commit()
        return jsonify({'message': 'Organization updated!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@organizations.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_organization(id):
    # Add role-based access control here if needed (e.g., only admin can delete)
    try:
        organization = Organization.query.get_or_404(id)
        db.session.delete(organization)
        db.session.commit()
        return jsonify({'message': 'Organization deleted!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@organizations.route('/<int:id>/donations', methods=['GET'])
@jwt_required()
def get_organization_donations(id):
    try:
        organization = Organization.query.get_or_404(id)
        donations = organization.donations
        total_donations = sum(d.amount for d in donations)
        
        non_anonymous_donations = []
        for d in donations:
            if not d.is_anonymous:
                # Ensure donor relationship is loaded
                donor_username = d.donor.username if d.donor else 'Unknown Donor'
                non_anonymous_donations.append({'donor': donor_username, 'amount': d.amount})
        
        anonymous_donations_total = sum(d.amount for d in donations if d.is_anonymous)
        
        return jsonify({
            'total_donations': total_donations,
            'non_anonymous_donations': non_anonymous_donations,
            'anonymous_donations_total': anonymous_donations_total
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

