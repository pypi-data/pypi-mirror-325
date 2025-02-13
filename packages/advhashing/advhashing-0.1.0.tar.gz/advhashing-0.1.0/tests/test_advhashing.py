import unittest
from advhashing import advhashing

class TestAdvHashing(unittest.TestCase):
    def test_hash_sha256(self):
        hash1 = advhashing.hash_sha256("test")
        hash2 = advhashing.hash_sha256("test")
        self.assertNotEqual(hash1, hash2)  # Salt should make hashes unique

    def test_hash_sha512(self):
        hash1 = advhashing.hash_sha512("test")
        hash2 = advhashing.hash_sha512("test")
        self.assertNotEqual(hash1, hash2)

    def test_hmac_sha256(self):
        mac = advhashing.hmac_sha256("key", "message")
        self.assertEqual(len(mac), 64)  # SHA-256 produces 64-character hex output

    def test_hmac_sha512(self):
        mac = advhashing.hmac_sha512("key", "message")
        self.assertEqual(len(mac), 128)  # SHA-512 produces 128-character hex output

    def test_multi_threaded_hash(self):
        hashes = advhashing.multi_threaded_hash(["data1", "data2"])
        self.assertEqual(len(hashes), 2)
        self.assertTrue(all(len(h) == 64 for h in hashes))  # SHA-256 produces 64 hex chars

if __name__ == "__main__":
    unittest.main()
