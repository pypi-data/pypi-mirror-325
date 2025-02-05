import unittest
from src.crypto import CsmxCrypto

class TestCsmxCrypto(unittest.TestCase):

    def test_generate_secure_hash(self):
        """Ensure that hashing generates a valid hex string"""
        data = "test_user"
        hashed_data = CsmxCrypto.generate_secure_hash(data)
        self.assertIsInstance(hashed_data, str)

    def test_generate_secure_token(self):
        """Ensure that a secure token is generated"""
        token = CsmxCrypto.generate_secure_token()
        self.assertIsInstance(token, str)
        self.assertEqual(len(token), 64)

if __name__ == '__main__':
    unittest.main()
