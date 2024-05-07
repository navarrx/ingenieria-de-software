from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.database import FULL_URL_DB
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app=Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.debug = True

    from app.resources import product
    app.register_blueprint(product, url_prefix='/api/v1/product')
    
    db.init_app(app)
    #Init app with cache
    #Cache.init_app(app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 300, 'CACHE_REDIS_HOST:': 'localhost', 'CACHE_REDIS_PORT': '6379', 'CACHE_REDIS_DB': '0', 'CACHE_REDIS_PASSWORD': 'Tisiano23', 'CACHE_KEY_PREFIX': 'test_'})


    return app
    