from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os



db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    # set up the database
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        
    # connect the db and migrate to our flask app
    db.init_app(app)
    migrate.init_app(app, db)

    # import routes
    from .routes import planet_bp, moon_bp
    
    # register the blueprint
    app.register_blueprint(planet_bp)
    app.register_blueprint(moon_bp)

    from app.models.planet import Planet
    from app.models.moon import Moon
    
    return app

