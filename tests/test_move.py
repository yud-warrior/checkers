import unittest

from checkers.move import Move


class MoveTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.move = Move((3, 4), [(5, 6), (7, 4)])
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_add(self) -> None:
        self.move.add((5, 2))
        self.assertEqual(self.move.steps[-1], (5, 2))

    def test___iter__(self) -> None:
        steps = [(5, 6), (7, 4)]
        for i, step in enumerate(self.move):
            self.assertEqual(step, steps[i])

    def test___next__(self) -> None:
        move_it = iter(self.move)
        steps = [(5, 6), (7, 4)]
        steps_it = iter(steps)
        self.assertEqual(next(move_it), next(steps_it))
        self.assertEqual(next(move_it), next(steps_it))
        with self.assertRaises(StopIteration):
            next(move_it)

    def test___str__(self) -> None:
        str_move = 'start: (3, 4)\tsteps: [(5, 6), (7, 4)]'
        self.assertEqual(str(self.move), str_move)
