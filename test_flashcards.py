# from unittest import TestCase
import unittest
from f_card import num_input
# import flashcards


class Test(unittest.TestCase):
    def test_num_input(self):
        self.assertIsInstance(num_input(), int)
        self.assertEqual(num_input(), 1)


if __name__ == '__main__':
    unittest.main()
