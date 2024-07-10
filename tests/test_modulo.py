import unittest

from src.modulo import add, subs

class TestModulo(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subs(self):
        self.assertEqual(subs(5, 2), 3)

if __name__ == '__main__':
    unittest.main