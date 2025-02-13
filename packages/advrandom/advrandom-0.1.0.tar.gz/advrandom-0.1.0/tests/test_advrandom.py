import unittest
from advrandom import advrandom

class TestAdvRandom(unittest.TestCase):
    def test_secure_randint(self):
        num = advrandom.secure_randint(1, 100)
        self.assertTrue(1 <= num <= 100)

    def test_secure_random_bytes(self):
        rand_bytes = advrandom.secure_random_bytes(16)
        self.assertEqual(len(rand_bytes), 16)

    def test_hash_entropy(self):
        hash1 = advrandom.hash_entropy("test")
        hash2 = advrandom.hash_entropy("test")
        self.assertNotEqual(hash1, hash2)  # Should always be different

    def test_multi_threaded_random(self):
        numbers = advrandom.multi_threaded_random(10)
        self.assertEqual(len(numbers), 10)
        self.assertTrue(all(isinstance(num, int) for num in numbers))

    def test_gaussian_random(self):
        num = advrandom.gaussian_random()
        self.assertIsInstance(num, float)

if __name__ == "__main__":
    unittest.main()
