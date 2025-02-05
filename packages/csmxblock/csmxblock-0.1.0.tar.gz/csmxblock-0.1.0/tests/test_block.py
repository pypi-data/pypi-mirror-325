import unittest
from src.block import CsmxBlock

class TestCsmxBlock(unittest.TestCase):

    def setUp(self):
        self.blockchain = CsmxBlock()
        self.user_data = "test_user"

    def test_generate_auth_block(self):
        """Ensure authentication block is created"""
        block = self.blockchain.generate_auth_block(self.user_data)
        self.assertIn("token", block)

    def test_validate_auth_block(self):
        """Ensure authentication block validation works"""
        block = self.blockchain.generate_auth_block(self.user_data)
        result = self.blockchain.validate_auth_block(self.user_data, block["token"])
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
