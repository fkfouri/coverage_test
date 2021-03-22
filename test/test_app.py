import unittest
from ..src.app import fibonacci, factorial

class TestFibonacci(unittest.TestCase):
    def test_fibonnacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonnacci_10(self):
        self.assertEqual(fibonacci(10), 89)

    def test_fibonnacci_30(self):
        self.assertEqual(fibonacci(30), 1346269)

class TestFactorial(unittest.TestCase):

    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_3(self):
        self.assertEqual(factorial(3), 6)

if __name__ == '__main__':
    #unittest.main()
    pass
