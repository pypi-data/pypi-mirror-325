import unittest
from advsecrets import advsecrets

class TestAdvSecrets(unittest.TestCase):
    def test_secure_token(self):
        token = advsecrets.secure_token(32)
        self.assertEqual(len(token), 64)  # Hex string length

    def test_secure_uuid(self):
        uuid = advsecrets.secure_uuid()
        self.assertEqual(len(uuid), 64)  # SHA-256 hex length

    def test_multi_threaded_tokens(self):
        tokens = advsecrets.multi_threaded_tokens(5)
        self.assertEqual(len(tokens), 5)
        self.assertTrue(all(len(t) == 64 for t in tokens))  # Each token is 64 hex chars

    def test_secure_password(self):
        password = advsecrets.secure_password(16)
        self.assertEqual(len(password), 16)  # Check length is correct

if __name__ == "__main__":
    unittest.main()
