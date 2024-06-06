import unittest
import redis
import os
import time
from dotenv import load_dotenv

class TestRedis(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        self.redis = redis.Redis(host='localhost', port=6379, db=0, password=os.getenv('PASSWORD'))
        self.redis.flushdb()  # Limpiar la base de datos de Redis antes de cada prueba

    def tearDown(self):
        self.redis.flushdb()  # Limpiar la base de datos de Redis después de cada prueba

    def test_redis_set_get(self):
        print("\n--- Test: Set and Get Value ---")
        self.redis.set('test', 'value')
        print("Set value: 'value'")
        
        value = self.redis.get('test')
        print(f"Get value: {value.decode()}")
        
        self.assertEqual(value, b'value')

    def test_redis_update_cache(self):
        print("\n--- Test: Update Cache ---")
        self.redis.set('test', 'value')
        print("Initial set value: 'value'")
        
        self.redis.set('test', 'new_value')
        print("Updated value to: 'new_value'")
        
        value = self.redis.get('test')
        print(f"Get updated value: {value.decode()}")
        
        self.assertEqual(value, b'new_value')

    def test_redis_delete_cache(self):
        print("\n--- Test: Delete Cache ---")
        self.redis.set('test', 'value')
        print("Set value: 'value'")
        
        self.redis.delete('test')
        print("Deleted key 'test'")
        
        value = self.redis.get('test')
        print(f"Get value after deletion: {value}")
        
        self.assertIsNone(value)

    def test_cache_effect(self):
        print("\n--- Test: Cache Effect ---")

        def get_data_from_cache(key):
            value = self.redis.get(key)
            if value is None:
                print(f"Cache miss for key '{key}'. Querying source database.")
                value = b'data_from_db'
                self.redis.set(key, value)
            else:
                print(f"Cache hit for key '{key}'.")
            return value

        # Primer acceso: debería obtener datos de la fuente de datos original
        value = get_data_from_cache('test')
        print(f"First access value: {value.decode()}")
        self.assertEqual(value, b'data_from_db')

        # Segundo acceso: debería obtener datos de la caché
        value = get_data_from_cache('test')
        print(f"Second access value: {value.decode()}")
        self.assertEqual(value, b'data_from_db')

        # Verificar que el valor en Redis es el esperado
        cached_value = self.redis.get('test')
        print(f"Cached value in Redis: {cached_value.decode()}")
        self.assertEqual(cached_value, b'data_from_db')

    def test_redis_timeout(self):
        print("\n--- Test: Redis Timeout ---")
        self.redis.set('temp_key', 'temp_value')
        self.redis.expire('temp_key', 2)  # Configurar el tiempo de vida de la clave a 2 segundos
        print("Set 'temp_key' with expiration of 2 seconds")
        
        value = self.redis.get('temp_key')
        print(f"Get value before timeout: {value.decode()}")
        self.assertEqual(value, b'temp_value')

        time.sleep(3)  # Esperar 3 segundos para que la clave expire

        value = self.redis.get('temp_key')
        print(f"Get value after timeout: {value}")
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()
