import unittest
from src.auth import CsmxAuth

class TestCsmxAuth(unittest.TestCase):

    def setUp(self):
        self.auth = CsmxAuth()
        self.user_data = "test_user"

    def test_generate_auth_token(self):
        """Ensure authentication token is generated"""
        token = self.auth.generate_auth_token(self.user_data)
        self.assertIsInstance(token, str)

    def test_verify_auth_token(self):
        """Ensure authentication token verification works"""
        token = self.auth.generate_auth_token(self.user_data)
        self.assertTrue(self.auth.verify_auth_token(self.user_data, token))

if __name__ == '__main__':
    unittest.main()
