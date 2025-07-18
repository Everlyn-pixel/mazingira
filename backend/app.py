from flask import Flask
from config import Config  # We'll set this up in config.py
from routes.main import main_bp  # This comes from routes/main.py

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
