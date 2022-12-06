import unittest

from src.checkers.game import Game, GameState, Color
from src.checkers.board import Cell


class GameTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game(4)
        self.game3 = Game(3)
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test__initial_black_count_1(self) -> None:
        self.assertEqual(self.game._initial_black_count(), 2)

    def test__initial_black_count_2(self) -> None:
        self.assertEqual(self.game3._initial_black_count(), 1)

    def test_opponent(self) -> None:
        self.assertIsInstance(self.game.opponent(), Color)
        self.assertEqual(self.game.opponent(), Color.WHITE)

    def test_get_all_moves(self) -> None:
        moves = self.game.get_all_moves()
        self.assertIsInstance(moves, list)
        self.assertEqual(len(moves), 3)
        self.assertIsInstance(moves[0].start, tuple)
        self.assertEqual(moves[0].start, (0, 1))
        self.assertIsInstance(moves[0].steps, list)
        self.assertEqual(len(moves[0].steps), 1)
        self.assertIsInstance(moves[0].steps[0], tuple)
        self.assertEqual(moves[0].steps[0], (1, 0))
        self.assertEqual(len(moves[1].steps), 1)
        self.assertEqual(len(moves[2].steps), 1)
        self.assertEqual(moves[1].steps[0], (1, 2))
        self.assertEqual(moves[2].steps[0], (1, 2))

    def test_make_move_1(self) -> None:
        moves = self.game.get_all_moves()
        move = moves[0]
        self.game.make_move(move)
        self.assertEqual(self.game.board.get_cell(0, 1), Cell.EMPTY)
        self.assertEqual(self.game.board.get_cell(1, 0), Cell.BLACK)
        self.assertEqual(self.game.turn, Color.WHITE)
        self.assertEqual(self.game.state, GameState.UNFINISHED)

    def test_make_move_2(self) -> None:
        while self.game.state == GameState.UNFINISHED:
            moves = self.game.get_all_moves()
            move = moves[0]
            self.game.make_move(move)

        self.assertEqual(self.game.state, GameState.WHITE_WON)
        self.assertEqual(self.game.board.get_cell(1, 0), Cell.WHITE)
        self.assertEqual(self.game.board.get_cell(0, 3), Cell.WHITE_QUEEN)
        self.assertEqual(self.game.black_count, 0)
        self.assertEqual(self.game.white_count, 2)

    def test_make_move_3(self) -> None:
        while self.game3.state == GameState.UNFINISHED:
            moves = self.game3.get_all_moves()
            move = moves[0]
            self.game3.make_move(move)

        self.assertEqual(self.game3.state, GameState.TIE)
        self.assertEqual(self.game3.black_count, 1)
        self.assertEqual(self.game3.white_count, 1)

    def test_undo_1(self) -> None:
        self.game.undo()
        self.assertEqual(self.game.turn, Color.BLACK)
        self.assertEqual(self.game.state, GameState.UNFINISHED)

    def test_undo_2(self) -> None:
        while self.game.state == GameState.UNFINISHED:
            moves = self.game.get_all_moves()
            move = moves[0]
            self.game.make_move(move)

        self.game.undo()
        self.assertEqual(self.game.state, GameState.UNFINISHED)
        self.assertEqual(self.game.board.get_cell(2, 1), Cell.BLACK)
        self.assertEqual(self.game.board.get_cell(3, 2), Cell.WHITE)
        self.assertEqual(self.game.board.get_cell(0, 3), Cell.WHITE_QUEEN)
        self.assertEqual(self.game.black_count, 1)
        self.assertEqual(self.game.white_count, 2)
