import unittest

from checkers.ai.random_ai import RandomAI
from checkers.game import Game, Color


class RandomAITestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.size = 8
        self.game = Game(self.size)
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_make_move_black_first_move(self) -> None:
        ai_color = Color.BLACK
        ai = RandomAI(self.size, ai_color)
        move = ai.make_move()
        self.game.make_move(move)
        self.assertEqual(self.game.turn, Color.WHITE)
        self.assertEqual(ai._game.turn, Color.WHITE)
        for row in range(self.size):
            for col in range(self.size):
                self.assertEqual(
                    self.game.board.get_cell(row, col),
                    ai._game.board.get_cell(row, col)
                )
        self.assertEqual(self.game.state, ai._game.state)
        self.assertEqual(self.game.black_count, ai._game.black_count)
        self.assertEqual(self.game.white_count, ai._game.white_count)
        self.assertEqual(self.game.tie_counter, ai._game.tie_counter)

    def test_make_move_white_first_move(self) -> None:
        ai_color = Color.WHITE
        ai = RandomAI(self.size, ai_color)
        move = self.game.get_all_moves()[0]
        self.game.make_move(move)
        move = ai.make_move(move)
        self.game.make_move(move)
        self.assertEqual(self.game.turn, Color.BLACK)
        self.assertEqual(ai._game.turn, Color.BLACK)
        for row in range(self.size):
            for col in range(self.size):
                self.assertEqual(
                    self.game.board.get_cell(row, col),
                    ai._game.board.get_cell(row, col)
                )
        self.assertEqual(self.game.state, ai._game.state)
        self.assertEqual(self.game.black_count, ai._game.black_count)
        self.assertEqual(self.game.white_count, ai._game.white_count)
        self.assertEqual(self.game.tie_counter, ai._game.tie_counter)
