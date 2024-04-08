from app.models.product import Product
from marshmallow import Schema,validate, fields, Schema, post_load

class ProductSchema(Schema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = fields.Integer(attribute='id', data_key='id')
    name = fields.String(attribute='name', data_key='name')
    price = fields.String(attribute='price', data_key='price')
    brand = fields.String(attribute='brand', data_key='brand')
    size = fields.String(attribute='size', data_key='size')
    stock = fields.String(attribute='stock', data_key='stock')

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)