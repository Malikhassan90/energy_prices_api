from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config
from .models import db
from .data_fetcher import populate_data
from flask import current_app
from flask_cors import CORS

# Initialize extensions
migrate = Migrate()

def create_app(config_name='development'):
    # Create the Flask app
    app = Flask(__name__, template_folder='templates')
    
    # Load the appropriate configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Import and register routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app

app = create_app()

# Populate data when the app is created
with app.app_context():
    db.create_all()
    populate_data()
