import unittest
from src import utils


class TestUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(utils.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(utils.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(utils.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(utils.divide(6, 2), 3)
        with self.assertRaises(ValueError):
            utils.divide(5, 0)
