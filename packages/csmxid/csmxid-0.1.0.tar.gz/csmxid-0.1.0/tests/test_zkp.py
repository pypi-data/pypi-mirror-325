import unittest
from src.zkp import CsmxZKP

class TestCsmxZKP(unittest.TestCase):

    def test_generate_zk_proof(self):
        """Ensure Zero-Knowledge Proofs are generated correctly"""
        data = "test_user"
        proof, secret = CsmxZKP.generate_zk_proof(data)
        self.assertIsInstance(proof, str)
        self.assertIsInstance(secret, bytes)

    def test_verify_zk_proof(self):
        """Ensure ZKP verification works"""
        data = "test_user"
        proof, secret = CsmxZKP.generate_zk_proof(data)
        self.assertTrue(CsmxZKP.verify_zk_proof(data, proof, secret))

if __name__ == '__main__':
    unittest.main()
