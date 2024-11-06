from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config


# Initialisation de SQLAlchemy
db = SQLAlchemy()




def create_app():
    app = Flask(__name__, template_folder='views/templates')
    app.config.from_object(Config)

    # Initialise db et login_manager avec l'application
    db.init_app(app)
    
    
    with app.app_context():
        # Crée les tables dans la base de données
        db.create_all()

        
        from .controllers.main import main
        
        # Enregistrement des blueprints
        app.register_blueprint(main)
        

    return app
