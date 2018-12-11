from flask import Flask
from flask_cors import CORS
from services.api.api_redirect import api_redirect_service

def create_app(debug=False):
    app = Flask(__name__)
    # Blueprint
    register_blueprints(app)

    CORS(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api_redirect_service)
