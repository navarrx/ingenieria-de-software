from flask import Flask, jsonify, request, Blueprint
#from flask_cors import CORSfrom app.models import *

def create_app():
    app=Flask(__name__)
    #CORS(app)


    #app.debug = True
    
    #db.init_app(app)
    #migrate.init_app(app, db)
    
    # from app.resources import home, client, product, product_brand
    # app.register_blueprint(home, url_prefix="/api/v1")
    # app.register_blueprint(client, url_prefix="/api/v1")
    # app.register_blueprint(product, url_prefix="/api/v1")
    # app.register_blueprint(product_brand, url_prefix="/api/v1")

    return app
    