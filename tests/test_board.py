import unittest

from checkers.board import Board, Cell


class BoardTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.board3x3 = Board(3)
        self.board6x6 = Board(6)
        self.board_default = Board()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_get_cell(self) -> None:
        self.assertEqual(self.board3x3.get_cell(0, 1), Cell.BLACK)
        self.assertEqual(self.board3x3.get_cell(0, 0), Cell.EMPTY)
        self.assertEqual(self.board3x3.get_cell(2, 1), Cell.WHITE)
        with self.assertRaises(IndexError):
            self.board3x3.get_cell(3, 1)

    def test_set_cell(self) -> None:
        self.board6x6.set_cell(3, 2, Cell.BLACK_QUEEN)
        self.assertEqual(self.board6x6.get_cell(3, 2), Cell.BLACK_QUEEN)
        with self.assertRaises(IndexError):
            self.board6x6.set_cell(7, 11, Cell.EMPTY)

    def test___str__(self) -> None:
        expected = "|------|\n" \
                   + "|__b __|\n" \
                   + "|  __  |\n" \
                   + "|__w __|\n" \
                   + "|------|\n"
        self.assertEqual(str(self.board3x3), expected)
