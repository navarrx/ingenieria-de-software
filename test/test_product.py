import unittest
import sys
import os

# Asegúrate de que puedes importar la aplicación correctamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Product
from app.services.product_services import ProductService

class ProductTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product_service = ProductService()

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.rollback()  # Hace rollback de la sesión en lugar de eliminar todas las tablas porque la anterior configuración fallaba
        self.app_context.pop()
    
    def test_create_product(self):
        entity = self.create_entity()
        self.assertTrue(entity.id)

    def create_entity(self):
        entity = Product(name="Coca Cola", price="300", brand="Coca Cola", size="200ml", stock="50")
        self.product_service.create(entity)
        return entity
    
    def test_delete_product(self):
        entity = self.create_entity()
        self.product_service.delete(entity.id)
        self.assertIsNone(Product.query.get(entity.id))
    
    def test_find_by_id_product(self):
        entity = self.create_entity()
        self.assertTrue(self.product_service.find_by_id(entity.id))
    
    def test_find_all_products(self):
        entity = self.create_entity()
        self.assertTrue(self.product_service.find_all())
    
    def test_update_product(self):
        entity = self.create_entity()
        entity.name = "Pepsi"
        self.product_service.update(entity, entity.id)
        self.assertEqual(Product.query.get(entity.id).name, "Pepsi")

if __name__ == '__main__':
    unittest.main()
