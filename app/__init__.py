from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.database import FULL_URL_DB
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
cache = Cache()

def create_app():
    app=Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.debug = True

    from app.resources import product
    app.register_blueprint(product, url_prefix='/api/v1/')
    
    db.init_app(app)
    migrate.init_app(app, db)
    #Init app with cache
    cache.init_app(app, config={'CACHE_TYPE': 'RedisCache', 'CACHE_DEFAULT_TIMEOUT': 300, 
                            'CACHE_REDIS_HOST': 'redis', 'CACHE_REDIS_PORT': 6379, 
                            'CACHE_REDIS_DB': '0', 'CACHE_REDIS_PASSWORD': 'Tisiano23', 
                            'CACHE_KEY_PREFIX': 'product_'})


    return app
    