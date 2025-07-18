from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return {"message": "Hello from Mazingira Backend!"}

@main_bp.route('/api/ping')
def ping():
    return {"message": "pong!"}
