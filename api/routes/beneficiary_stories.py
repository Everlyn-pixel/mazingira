from flask import Blueprint, request, jsonify
from extensions import db
from models.story import Story
from models.beneficiary import Beneficiary
from flask_jwt_extended import jwt_required

beneficiary_stories = Blueprint('beneficiary_stories', __name__, url_prefix='/beneficiaries/<int:beneficiary_id>/stories')

@beneficiary_stories.route('/', methods=['GET'])
@jwt_required()
def get_stories_for_beneficiary(beneficiary_id):
    try:
        beneficiary = Beneficiary.query.get_or_404(beneficiary_id)
        stories = beneficiary.stories
        return jsonify([{'id': story.id, 'title': story.title, 'content': story.content, 'created_at': story.created_at} for story in stories]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@beneficiary_stories.route('/', methods=['POST'])
@jwt_required()
def create_story_for_beneficiary(beneficiary_id):
    data = request.get_json()
    if not data or not all(key in data for key in ['title', 'content']):
        return jsonify({'error': 'Missing data for story creation'}), 400
    try:
        beneficiary = Beneficiary.query.get_or_404(beneficiary_id)
        new_story = Story(title=data['title'], content=data['content'], beneficiary_id=beneficiary.id, organization_id=beneficiary.organization_id)
        db.session.add(new_story)
        db.session.commit()
        return jsonify({'message': 'New story created!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@beneficiary_stories.route('/<int:story_id>', methods=['DELETE'])
@jwt_required()
def delete_story(beneficiary_id, story_id):
    try:
        story = Story.query.filter_by(id=story_id, beneficiary_id=beneficiary_id).first_or_404()
        db.session.delete(story)
        db.session.commit()
        return jsonify({'message': 'Story deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
