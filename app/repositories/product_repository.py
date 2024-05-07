from app.models.product import Product
from app.repositories.base_repository import BaseRepository

class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__(Product)
        from app import db
        self.__model = Product
        self.__db = db
        
    def find_by_name(self, name) -> Product:
        return self.__db.session.query(self.__model).filter_by(name=name).first()
    
    def find_by_brand(self, brand) -> Product:
        return self.__db.session.query(self.__model).filter_by(brand=brand).first()

    def update(self, entity: Product, id: int):
        try:
            existing_entity = self.__db.session.query(self.__model).get(id)
            if existing_entity:
                existing_entity.name = entity.name
                existing_entity.price = entity.price
                existing_entity.brand = entity.brand
                existing_entity.size = entity.size
                existing_entity.stock = entity.stock
                self.__db.session.commit()
                return existing_entity
            else:
                return None
        except Exception as e:
            self.__db.session.rollback()
            raise e
