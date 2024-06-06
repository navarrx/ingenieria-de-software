import unittest
from app import create_app, db
from app.models import Product
from app.services.product_services import ProductService

class ProductTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product_service = ProductService()

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_product_create(self):
        product = Product(name="Test Product", price=10, brand="Test Brand", size="Test Size", stock=50)
        self.product_service.create(product)
        self.assertIsNotNone(product)

    def test_product_find_by_id(self):
        product = Product(name="Test Product", price=10, brand="Test Brand", size="Test Size", stock=50)
        self.product_service.create(product)
        self.product_service.find_by_id(product.id)
        self.assertIsNotNone(product)

    def test_product_find_by_name(self):
        product = Product(name="Test Product", price=10, brand="Test Brand", size="Test Size", stock=50)
        product_name = product.name
        self.product_service.create(product)
        self.product_service.find_by_name(product_name)
        self.assertIsNotNone(product)
        self.assertEqual(product.name, "Test Product")

    def test_product_find_by_brand(self):
        product = Product(name="Test Product", price=10, brand="Test Brand", size="Test Size", stock=50)
        product_brand = product.brand
        self.product_service.create(product)
        self.product_service.find_by_brand(product_brand)
        self.assertIsNotNone(product)
        self.assertEqual(product.brand, "Test Brand")

    def test_product_update(self):
        product = Product(name='Test Product', price=10, brand='Test Brand', size='Test Size', stock=50)
        db.session.add(product)
        db.session.commit()
        product.name = 'Updated Test Product'
        self.product_service.update(product, product.id)
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'Updated Test Product')

    def test_product_delete(self):
        product = Product(name='Test Product', price=10, brand='Test Brand', size='Test Size', stock=50)
        db.session.add(product)
        db.session.commit()
        result = self.product_service.delete(product.id)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()