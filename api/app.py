from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
import os
from dotenv import load_dotenv
from extensions import db, jwt

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "methods": "*"}})
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)

    from routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')

    return app

from app import create_app
from extensions import db
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
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app = create_app()
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(organizations_blueprint)
app.register_blueprint(donations_blueprint)
app.register_blueprint(stories_blueprint)
app.register_blueprint(beneficiaries_blueprint)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Organization': Organization, 'Donation': Donation, 'Story': Story, 'Beneficiary': Beneficiary}

app = create_app()
