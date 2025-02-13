import unittest
from advjson import advjson

class TestAdvJson(unittest.TestCase):
    def test_compress_decompress(self):
        data = {"key": "value"}
        compressed = advjson.compress_json(data)
        decompressed = advjson.decompress_json(compressed)
        self.assertEqual(data, decompressed)

    def test_encrypt_decrypt(self):
        data = {"secure": "data"}
        key = advjson.generate_key()
        encrypted = advjson.encrypt_json(data, key)
        decrypted = advjson.decrypt_json(encrypted, key)
        self.assertEqual(data, decrypted)

    def test_validate_json(self):
        data = {"name": "Alice", "age": 25}
        schema = {"type": "object", "properties": {"name": {"type": "string"}, "age": {"type": "number"}}}
        self.assertTrue(advjson.validate_json(data, schema))

    def test_multi_threaded_compression(self):
        data_list = [{"key": f"value{i}"} for i in range(5)]
        compressed_list = advjson.multi_threaded_compression(data_list)
        self.assertEqual(len(compressed_list), 5)

if __name__ == "__main__":
    unittest.main()
