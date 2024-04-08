import unittest
from app import create_app, db
from app.models import Product

class ProductTestCase(unittest.TestCase):
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
        db.session.add(product)
        db.session.commit()
        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10)
        self.assertEqual(product.brand, "Test Brand")
        self.assertEqual(product.size, "Test Size")
        self.assertEqual(product.stock, 50)

    def test_product_update(self):
        product = Product(name="Test Product", price=10, brand="Test Brand", size="Test Size", stock=50)
        db.session.add(product)
        db.session.commit()
        product.name = "Updated Product"
        product.price = 20
        product.brand = "Updated Brand"
        product.size = "Updated Size"
        product.stock = 100
        db.session.commit()
        self.assertEqual(product.name, 'Updated Product')
        self.assertEqual(product.price, 20)
        self.assertEqual(product.brand, 'Updated Brand')
        self.assertEqual(product.size, 'Updated Size')
        self.assertEqual(product.stock, 100)

    def test_product_delete(self):
        product = Product(name='Test Product', price=10, brand='Test Brand', size='Test Size', stock=50)
        db.session.add(product)
        db.session.commit()
        db.session.delete(product)
        db.session.commit()
        self.assertIsNone(Product.query.get(product.id))

if __name__ == '__main__':
    unittest.main()
