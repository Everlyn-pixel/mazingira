from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
import os
from dotenv import load_dotenv
from extensions import db, jwt
from models.user import User
from models.organization import Organization
from models.donation import Donation
from models.story import Story
from models.beneficiary import Beneficiary
from routes.main import main as main_blueprint
from routes.auth import auth as auth_blueprint
from routes.organizations import organizations as organizations_blueprint
from routes.donations import donations as donations_blueprint
from routes.stories import stories as stories_blueprint
from routes.beneficiaries import beneficiaries as beneficiaries_blueprint

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "methods": "*"}})
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
    app.register_blueprint(organizations_blueprint, url_prefix='/api/organizations')
    app.register_blueprint(donations_blueprint, url_prefix='/api/donations')
    app.register_blueprint(stories_blueprint, url_prefix='/api/stories')
    app.register_blueprint(beneficiaries_blueprint, url_prefix='/api/beneficiaries')

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Organization': Organization, 'Donation': Donation, 'Story': Story, 'Beneficiary': Beneficiary}

    return app

app = create_app()