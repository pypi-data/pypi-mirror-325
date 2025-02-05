import unittest
from src.did import CsmxID

class TestCsmxID(unittest.TestCase):

    def setUp(self):
        self.identity_system = CsmxID()
        self.user_data = "test_user"

    def test_create_identity(self):
        """Ensure identity creation returns a valid token"""
        token, proof = self.identity_system.create_identity(self.user_data)
        self.assertIsInstance(token, str)
        self.assertIsInstance(proof, str)

    def test_verify_identity(self):
        """Ensure identity verification works"""
        token, proof = self.identity_system.create_identity(self.user_data)
        result = self.identity_system.verify_identity(self.user_data, token, proof)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
