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

    CORS(app)
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)

    return app

