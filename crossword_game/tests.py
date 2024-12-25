import unittest
import os
from crossword_game.game import Crossword

class TestCrossword(unittest.TestCase):

    def setUp(self):
        self.crossword = Crossword(5)

    def test_add_word_horizontal(self):
        result = self.crossword.add_word("hello", 0, 0, "horizontal")
        self.assertTrue(result)
        self.assertEqual(self.crossword.board[0], ['h', 'e', 'l', 'l', 'o'])

    def test_add_word_vertical(self):
        result = self.crossword.add_word("world", 0, 0, "vertical")
        self.assertTrue(result)
        self.assertEqual([self.crossword.board[i][0] for i in range(5)], ['w', 'o', 'r', 'l', 'd'])

    def test_add_word_overlap(self):
        self.crossword.add_word("hello", 0, 0, "horizontal")
        result = self.crossword.add_word("hero", 0, 0, "vertical")
        self.assertTrue(result)
        self.assertEqual(self.crossword.board[0], ['h', 'e', 'l', 'l', 'o'])
        self.assertEqual([self.crossword.board[i][0] for i in range(4)], ['h', 'e', 'r', 'o'])

    def test_add_word_invalid(self):
        result = self.crossword.add_word("invalid", 0, 0, "horizontal")
        self.assertFalse(result)

    def test_is_valid_word(self):
        self.crossword.add_word("hello", 0, 0, "horizontal")
        self.assertTrue(self.crossword.is_valid_word("hello"))
        self.assertFalse(self.crossword.is_valid_word("world"))

    def test_display_board(self):
        self.crossword.add_word("hello", 0, 0, "horizontal")
        self.crossword.add_word("world", 1, 0, "vertical")
        self.crossword.display_board()

if __name__ == '__main__':
    unittest.main()
