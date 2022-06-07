# -*- coding: utf-8 -*-
"""This module contains initialization code for the api package."""
import os
import sys

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from .blueprints.default.views import default
from .blueprints.extensions import db
from .helpers import are_flask_environment_variable_set

load_dotenv()


def create_app():
    """Create the Flask app."""
    if are_flask_environment_variable_set():
        app = Flask(__name__)
        app.register_blueprint(default)

        if os.getenv('FLASK_ENV') == 'production':  # pragma: no cover
            app.config.from_object('api.config.ProductionConfig')
        elif os.getenv('FLASK_ENV') == 'development':  # pragma: no cover
            app.config.from_object('api.config.DevelopmentConfig')
        elif os.getenv('FLASK_ENV') == 'stage':  # pragma: no cover
            app.config.from_object('api.config.StagingConfig')
        elif os.getenv('FLASK_ENV') == 'test':
            app.config.from_object('api.config.TestingConfig')
        else:
            app.config.from_object('api.config.DevelopmentConfig')

        print(f"The configuration used is for {os.environ['FLASK_ENV']} environment.")
        print(f"The database connection string is {app.config['SQLALCHEMY_DATABASE_URI']}.")

        db.init_app(app=app)
        migrate = Migrate()
        migrate.init_app(app, db)

        return app

    print('Application existing...')
    sys.exit(1)
