from app.repositories import ProductRepository

class ProductService:
    def __init__(self):
        self.__repo=ProductRepository()

    def find_by_id(self, product_id):
        return self.__repo.find_by_id(product_id)
    
    def find_by_name(self, name):
        return self.__repo.find_by_name(name)

    def find_by_brand(self, brand):
        return self.__repo.find_by_brand(brand)
    
    def find_all(self):
        return self.__repo.find_all()

    def update(self, product, product_id):
            return self.__repo.update(product, product_id)
    
    def delete(self, product_id):
        return self.__repo.delete(product_id)
    
    def create(self, product):
        return self.__repo.create(product)
