from app.models.product import Product
from marshmallow import Schema,validate, fields, Schema, post_load

class ProductSchema(Schema):
    id = fields.Int(load_only=True)
    name = fields.Str(required=True)
    price = fields.Str(required=True)
    brand = fields.Str(required=True)
    size = fields.Str(required=True)
    stock = fields.Str(required=True)

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)