from flask import Blueprint, request, jsonify
from extensions import db
from models.story import Story

stories = Blueprint('stories', __name__, url_prefix='/stories')

@stories.route('/', methods=['GET', 'POST'])
def handle_stories():
    if request.method == 'POST':
        data = request.get_json()
        new_story = Story(title=data['title'], content=data['content'], organization_id=data['organization_id'])
        db.session.add(new_story)
        db.session.commit()
        return jsonify({'message': 'New story created!'})
    else:
        stories = Story.query.all()
        return jsonify([{'title': story.title, 'content': story.content, 'organization_id': story.organization_id} for story in stories])
