import unittest

from checkers.move import Move, WrongMoveError


class MoveTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.move = Move((3, 4), [(5, 6), (7, 4)])
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_add(self) -> None:
        self.move.add((5, 2))
        self.assertEqual(self.move.steps[-1], (5, 2))
