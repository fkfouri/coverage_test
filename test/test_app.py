import unittest
from ..src.app import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonnacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonnacci_10(self):
        self.assertEqual(fibonacci(10), 89)

    def test_fibonnacci_30(self):
        self.assertEqual(fibonacci(30), 1346269)

if __name__ == '__main__':
    unittest.main()
