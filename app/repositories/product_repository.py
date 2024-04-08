from app.models.product import *
from app import db
from app.repositories.base_repository import BaseRepository
from app.config.database import db

class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__(Product)
        self.__model = Product

    def find_by_brand(self, brand) -> Product:
        return db.session.query(self.__model).filter_by(brand=brand).first()

    def update(self, entity: db.Model, id: int):
        try:
            existing_entity = db.session.query(self.__model).get(id)
            if existing_entity:
                existing_entity.name = entity.name
                existing_entity.price = entity.price
                existing_entity.brand = entity.brand
                existing_entity.size = entity.size
                existing_entity.stock = entity.stock
                db.session.commit()
                return existing_entity
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise e
            
