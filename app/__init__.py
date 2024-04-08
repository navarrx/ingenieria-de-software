from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_cors import CORS
from app.config.database import FULL_URL_DB

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app=Flask(__name__)
    #CORS(app)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.debug = True
    
    db.init_app(app)
    #migrate.init_app(app, db)

    #with app.app_context():
    #    db.create_all()

    return app
    