from app import db
from dataclasses import dataclass

@dataclass
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(50))
    price = db.Column('price', db.Float)
    brand = db.Column('brand', db.String(50))
    size = db.Column('size', db.String(50))
    stock = db.Column('stock', db.Float)