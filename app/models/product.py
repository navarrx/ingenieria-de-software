from app import db
from dataclasses import dataclass
from sqlalchemy import Column

@dataclass
class Product(db.Model):
    __tablename__ = 'product'

    id = Column(db.Integer, primary_key=True, autoincrement=True)
    name = Column(db.String(50))
    price = Column(db.Float(50))
    brand = Column(db.String(50))
    size = Column(db.String(50))
    stock = Column(db.Float(50))

    def __init__(self, name, price, brand, size, stock):
        self.name = name
        self.price = price
        self.brand = brand
        self.size = size
        self.stock = stock