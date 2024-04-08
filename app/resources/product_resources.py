from flask import Blueprint, jsonify, request
from app.services.product_services import ProductService
from app.mapping.product_schema import ProductSchema

schema = ProductSchema()
product=Blueprint('product',__name__)

