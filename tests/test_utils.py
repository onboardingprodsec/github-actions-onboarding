import unittest
from src import utils


class TestUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(utils.add(1, 2), 3)
