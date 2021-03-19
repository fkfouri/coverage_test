import unittest
from app import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonnacci_1(self):
        self.assertEqual(fibonacci(1), 1)

if __name__ == '__main__':
    unittest.main()
