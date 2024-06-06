from app.repositories import ProductRepository
from app import cache

class ProductService:
    def __init__(self):
        self.__repo=ProductRepository()

    def find_by_id(self, product_id):
        product = cache.get(f'{product_id}')
        if product is None:
            product = self.__repo.find_by_id(product_id)
            cache.set(f'{product_id}', product, timeout = 50)
        return product
    
    def find_by_name(self, name):
        product = cache.get(f'{name}')
        if product is None:
            product = self.__repo.find_by_name(name)
            cache.set(f'{name}', product, timeout = 50)
        return product

    def find_by_brand(self, brand):
        product = cache.get(f'{brand}')
        if product is None:
            product = self.__repo.find_by_brand(brand)
            cache.set(f'{brand}', product, timeout = 50)
        return product
    
    def find_all(self):
        return self.__repo.find_all()

    def update(self, product, product_id):
            return self.__repo.update(product, product_id)
    
    def delete(self, product_id):
        return self.__repo.delete(product_id)
    
    def create(self, product):
        product = self.__repo.create(product)
        cache.set(f'{product.id}', product, timeout = 50)
        return product
