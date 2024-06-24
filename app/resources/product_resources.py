from flask import Blueprint, jsonify, request
from app.mapping.product_schema import ProductSchema

schema = ProductSchema()
product=Blueprint('product',__name__)

@product.route('/', methods=['GET'])
def index():
    return {"message":"Welcome to the product API!"}, 200

@product.route('/product/<string:product_id>', methods=['GET'])
def get_product(product_id):
    from app.services.product_services import ProductService
    product = ProductService().find_by_id(product_id)
    product_data = schema.dump(product)
    product_data['id'] = product.id

    return jsonify(product_data), 200

@product.route('/product/brand/<string:brand>', methods=['GET'])
def get_product_by_brand(brand):
    from app.services.product_services import ProductService
    product = ProductService().find_by_brand(brand)
    return jsonify(schema.dump(product)), 200

@product.route('/product/all', methods=['GET'])
def get_all_products():
    from app.services.product_services import ProductService
    products = ProductService().find_all()
    return jsonify(schema.dump(products, many=True)), 200

@product.route('/product/create', methods=['POST'])
def create_product():
    from app.services.product_services import ProductService
    product = ProductService().create(schema.load(request.json))
    return {"product":schema.dump(product)}, 201

@product.route('/product/update/<string:product_id>', methods=['PUT'])
def update_product(product_id):
    from app.services.product_services import ProductService
    updated_product = ProductService().update(schema.load(request.json), product_id)
    if updated_product is None:
        return {"error": "Client not found"}, 404
    else:
        return jsonify(schema.dump(updated_product)), 200

@product.route('/product/delete/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    from app.services.product_services import ProductService
    return jsonify(ProductService().delete(product_id)), 200