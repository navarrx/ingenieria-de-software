import unittest
from flask import current_app
from app import create_app
from app.models.product import Product


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_product(self):
        product = Product
        product.name = "Coca Cola"
        self.assertEqual(product.name, "Coca Cola")

if __name__ == '__main__':
    unittest.main()