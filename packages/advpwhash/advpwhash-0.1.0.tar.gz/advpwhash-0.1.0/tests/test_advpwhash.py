import unittest
from advpwhash import advpwhash

class TestAdvPwHash(unittest.TestCase):
    def test_bcrypt_hash_verify(self):
        password = "SecurePassword123"
        hashed = advpwhash.bcrypt_hash(password)
        self.assertTrue(advpwhash.bcrypt_verify(password, hashed))

    def test_argon2_hash_verify(self):
        password = "SecurePassword456"
        hashed = advpwhash.argon2_hash(password)
        self.assertTrue(advpwhash.argon2_verify(password, hashed))

    def test_multi_threaded_bcrypt(self):
        passwords = ["pass1", "pass2", "pass3"]
        hashed_list = advpwhash.multi_threaded_bcrypt(passwords)
        self.assertEqual(len(hashed_list), len(passwords))

if __name__ == "__main__":
    unittest.main()
