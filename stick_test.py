import unittest
from sticks.py import *

class TestSticks(unittest.TestCase):
​   def test_game_loop(self):
        # self.assertEqual(easy_words(word_list),
        # easy_words_list = []
        self.assertTrue(is_game_over(-5))​
        self.assertTrue(is_game_over(-1))
        self.assertTrue(is_game_over(0))
        self.assertFalse(is_game_over(1))
        self.assertFalse(is_game_over(2))
        self.assertFalse(is_game_over(3))
        self.assertFalse(is_game_over(50))
        pass
​
​
if __name__ == '__main__':
    unittest.main()
