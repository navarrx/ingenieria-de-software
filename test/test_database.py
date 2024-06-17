import unittest
import psycopg2
import os
from dotenv import load_dotenv

class TestDatabase(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.connection = psycopg2.connect(
            host='postgresql.product.localhost',
            port=5432,
            user=os.getenv('USER_DB'),
            password=os.getenv('PASS_DB'),
            database=os.getenv('NAME_DB')
        )
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_database_connection(self):
        print("\n--- Testing the Database Connection ---")
        self.assertIsNotNone(self.connection)

if __name__ == "__main__":
    unittest.main()