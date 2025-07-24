from flask import Blueprint, request, jsonify
from extensions import db
from models.story import Story
from flask_jwt_extended import jwt_required, get_jwt_identity

stories = Blueprint('stories', __name__, url_prefix='/stories')

@stories.route('/', methods=['GET', 'POST'])
@jwt_required()
def handle_stories():
    current_user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        if not data or not all(key in data for key in ['title', 'content', 'organization_id']):
            return jsonify({'error': 'Missing data for story creation'}), 400
        try:
            new_story = Story(title=data['title'], content=data['content'], organization_id=data['organization_id'])
            db.session.add(new_story)
            db.session.commit()
            return jsonify({'message': 'New story created!'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else: # GET request
        try:
            stories = Story.query.all()
            return jsonify([{'id': story.id, 'title': story.title, 'content': story.content, 'organization_id': story.organization_id, 'created_at': story.created_at} for story in stories]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
