import unittest
from advhashlib import advhashlib

class TestAdvHashLib(unittest.TestCase):
    def test_sha256(self):
        hash1 = advhashlib.sha256("test")
        hash2 = advhashlib.sha256("test")
        self.assertNotEqual(hash1, hash2)  # Salt should change hash

    def test_sha512(self):
        hash1 = advhashlib.sha512("test")
        hash2 = advhashlib.sha512("test")
        self.assertNotEqual(hash1, hash2)  # Should be different

    def test_hmac_sha256(self):
        mac = advhashlib.hmac_sha256("key", "message")
        self.assertEqual(len(mac), 64)  # HMAC SHA-256 should be 64 chars

    def test_multi_threaded_hash(self):
        hashes = advhashlib.multi_threaded_hash(["data1", "data2"])
        self.assertEqual(len(hashes), 2)
        self.assertTrue(all(len(h) == 64 for h in hashes))  # SHA-256 is 64 hex chars

if __name__ == "__main__":
    unittest.main()
